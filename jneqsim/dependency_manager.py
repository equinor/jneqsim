"""
NeqSim Dependency Manager

Handles resolution and downloading of NeqSim Java dependencies from GitHub releases.
"""

import logging
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

import yaml

from .jar_cache import JARCacheManager


class NeqSimDependencyManager:
    """Manages NeqSim JAR dependencies from GitHub releases"""

    def __init__(self, config_path: Optional[Path] = None, cache_dir: Optional[Path] = None):
        """
        Initialize dependency manager

        Args:
            config_path: Path to dependencies.yaml, defaults to package config
            cache_dir: Directory for caching version info, defaults to ~/.jneqsim/cache
        """
        if config_path is None:
            config_path = Path(__file__).parent / "dependencies.yaml"

        if cache_dir is None:
            cache_dir = Path.home() / ".jneqsim" / "cache"

        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.config = self._load_config(config_path)
        self.logger = self._setup_logging()

        # Initialize cache manager
        self.cache_manager = JARCacheManager(self.cache_dir, self.config, self.logger)

    def _load_config(self, config_path: Path) -> dict:
        """Load configuration from YAML file"""
        with open(config_path) as f:
            return yaml.safe_load(f)

    def _setup_logging(self) -> logging.Logger:
        """Setup logging based on configuration"""
        logger = logging.getLogger(__name__)
        level = getattr(logging, self.config["logging"]["level"])
        logger.setLevel(level)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def _get_jar_patterns(self, java_version: int) -> list[str]:
        """Get list of JAR filename patterns to try for a given Java version.

        Returns patterns in order of preference, with newer patterns first.
        Some releases use varying naming patterns (e.g., Java21-Java21 vs Java21).
        """
        github_config = self.config["neqsim"]["sources"]["github"]

        if java_version == 8:
            return [
                "neqsim-{version}-Java8-Java8.jar",  # Newer pattern
                github_config["assets"]["java8"],  # Standard pattern
                github_config["assets"]["java11"],  # Fallback
            ]
        elif 11 <= java_version < 21:
            return [
                "neqsim-{version}.jar",  # Standard pattern
                github_config["assets"]["java11"],  # Fallback to default
            ]
        elif java_version >= 21:
            return [
                "neqsim-{version}-Java21-Java21.jar",  # Newer pattern
                github_config["assets"]["java21"],  # Standard pattern
                github_config["assets"]["java11"],  # Fallback to default
            ]
        else:
            return [github_config["assets"]["java11"]]

    def _get_JAR_from_github(self, version: str, java_version: int) -> Path:
        """Download JAR from GitHub releases with fallback support and caching"""
        github_config = self.config["neqsim"]["sources"]["github"]

        # Check cache first
        cached_jar = self.cache_manager.get_cached_jar(version, java_version)
        if cached_jar:
            return cached_jar

        patterns_to_try = self._get_jar_patterns(java_version)

        # Try each pattern until one succeeds
        last_error = None
        for i, asset_pattern in enumerate(patterns_to_try):
            jar_filename = asset_pattern.format(version=version)
            url = f"{github_config['base_url']}/v{version}/{jar_filename}"

            # Create temporary directory for download
            import tempfile

            temp_dir = Path(tempfile.mkdtemp(prefix="jneqsim_"))
            downloaded_jar = temp_dir / jar_filename

            try:
                is_fallback = i > 0
                if self.config["logging"]["show_progress"]:
                    if is_fallback:
                        self.logger.info(f"Trying fallback: {jar_filename} for Java {java_version}...")
                    else:
                        self.logger.info(f"Downloading {jar_filename} for Java {java_version}...")

                with urllib.request.urlopen(url) as response:  # noqa: S310
                    content = response.read()

                downloaded_jar.write_bytes(content)

                if is_fallback:
                    self.logger.warning(
                        f"Using fallback JAR '{jar_filename}' for Java {java_version}. "
                        f"Java {java_version}-specific version not available."
                    )
                else:
                    self.logger.info(f"Downloaded from GitHub: {downloaded_jar.name}")

                # Cache the downloaded JAR
                cached_jar = self.cache_manager.cache_jar(downloaded_jar, version, java_version)
                return cached_jar

            except urllib.error.HTTPError as e:
                if e.code == 404:
                    last_error = e
                    self.logger.debug(f"JAR not found: {jar_filename} (trying fallback...)")
                    continue  # Try next pattern
                else:
                    # For other HTTP errors, fail immediately
                    self.logger.error(f"HTTP error downloading from GitHub: {e}")
                    raise RuntimeError(f"Could not download NeqSim from GitHub: {e}") from e
            except Exception as e:
                last_error = e
                self.logger.error(f"Failed to download from GitHub: {e}")
                # For non-HTTP errors, try fallback
                continue

        # If we get here, all attempts failed
        error_msg = f"Could not download NeqSim from GitHub for Java {java_version}: {last_error}"
        self.logger.error(error_msg)
        raise RuntimeError(error_msg) from last_error

    def resolve_dependency(self, java_version: Optional[int] = None) -> Path:
        """
        Resolve NeqSim dependency

        Args:
            version: Specific NeqSim version to use. If None, uses the version
                    configured in dependencies.yaml. Note: The config should specify
                    a pinned version that has been tested with this jneqsim release.
            java_version: Java version, auto-detected if None

        Returns:
            Path to resolved JAR file
        """

        neqsim_version = self.config["neqsim"]["version"]
        if neqsim_version is None:
            raise ValueError("NeqSim version must be specified either as an argument or in dependencies.yaml")

        java_version = self._resolve_java_version(java_version)

        # Download dependency
        jar_path = self._get_JAR_from_github(neqsim_version, java_version)

        return jar_path

    def _resolve_java_version(self, java_version: Optional[int]) -> int:
        """Resolve the Java version to use"""
        if java_version is not None:
            return java_version

        try:
            import jpype

            if jpype.isJVMStarted():
                return jpype.getJVMVersion()[0]
            else:
                return 11  # Default fallback
        except ImportError:
            return 11  # Default fallback

    @property
    def jar_cache_dir(self) -> Path:
        """Access to JAR cache directory for backward compatibility"""
        return self.cache_manager.jar_cache_dir
