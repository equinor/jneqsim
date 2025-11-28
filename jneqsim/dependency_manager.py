"""
NeqSim Dependency Manager

Handles resolution and downloading of NeqSim Java dependencies from GitHub releases.
"""

import json
import logging
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

import yaml


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

        self.jar_cache_dir = self.cache_dir / "jars"
        self.jar_cache_dir.mkdir(parents=True, exist_ok=True)


        self.config = self._load_config(config_path)
        self.logger = self._setup_logging()

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

    # def get_latest_version(self) -> str:
    #     """Get latest NeqSim version from GitHub API with caching and fallback"""
    #     cache_file = self.cache_dir / "latest_version.json"
    #     repo = self.config["neqsim"]["sources"]["github"]["repository"]
    #     url = f"https://api.github.com/repos/{repo}/releases/latest"

    #     try:
    #         with urllib.request.urlopen(url, timeout=10) as response:  # noqa: S310
    #             data = json.loads(response.read())
    #             version = data["tag_name"].lstrip("v")
    #             self.logger.debug(f"Latest version from GitHub: {version}")

    #             # Cache the version with timestamp
    #             cache_data = {"version": version, "timestamp": __import__("time").time()}
    #             cache_file.write_text(json.dumps(cache_data, indent=2))

    #             return version
    #     except urllib.error.HTTPError as e:
    #         if e.code == 403:  # Rate limit exceeded
    #             self.logger.warning("GitHub rate limit exceeded, trying cached or fallback version")
    #             return self._get_fallback_version(cache_file)
    #         else:
    #             self.logger.error(f"HTTP error getting latest version: {e}")
    #             return self._get_fallback_version(cache_file)
    #     except Exception as e:
    #         self.logger.warning(f"Failed to get latest version from GitHub: {e}")
    #         return self._get_fallback_version(cache_file)

    # def _get_fallback_version(self, cache_file: Path) -> str:
    #     """Get version from cache or use configured fallback"""
    #     self.logger.info("Trying to get version from cache or fallback")
    #     # Try cached version first
    #     if cache_file.exists():
    #         try:
    #             cache_data = json.loads(cache_file.read_text())
    #             version = cache_data["version"]
    #             self.logger.info(f"Using cached version: {version}")
    #             return version
    #         except Exception as e:
    #             self.logger.warning(f"Failed to read cached version: {e}")

    #     # Use fallback version from config
    #     fallback = self.config["neqsim"].get("fallback_version")
    #     if fallback:
    #         self.logger.info(f"Using fallback version from config: {fallback}")
    #         return fallback

    #     # Last resort - raise error
    #     raise RuntimeError(
    #         "Could not determine NeqSim version: GitHub API unavailable, "
    #         "no cached version, and no fallback version configured"
    #     )

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

    def _get_from_github(self, version: str, java_version: int) -> Path:
        github_config = self.config["neqsim"]["sources"]["github"]
        patterns_to_try = self._get_jar_patterns(java_version)

        last_error = None
        for i, asset_pattern in enumerate(patterns_to_try):
            jar_filename = asset_pattern.format(version=version)
            url = f"{github_config['base_url']}/v{version}/{jar_filename}"

            # Check persistent cache first
            cached_jar = self.jar_cache_dir / jar_filename
            if cached_jar.exists():
                self.logger.info(f"Using cached JAR: {cached_jar}")
                return cached_jar

            try:
                is_fallback = i > 0
                if self.config["logging"]["show_progress"]:
                    if is_fallback:
                        self.logger.info(f"Trying fallback: {jar_filename} for Java {java_version}...")
                    else:
                        self.logger.info(f"Downloading {jar_filename} for Java {java_version}...")

                with urllib.request.urlopen(url) as response:
                    content = response.read()

                # Save to persistent cache
                cached_jar.write_bytes(content)
                self.logger.info(f"Downloaded and cached JAR: {cached_jar}")

                if is_fallback:
                    self.logger.warning(
                        f"Using fallback JAR '{jar_filename}' for Java {java_version}. "
                        f"Java {java_version}-specific version not available."
                    )
                else:
                    self.logger.info(f"Downloaded from GitHub: {cached_jar.name}")

                return cached_jar

            except urllib.error.HTTPError as e:
                if e.code == 404:
                    last_error = e
                    self.logger.debug(f"JAR not found: {jar_filename} (trying fallback...)")
                    continue  # Try next pattern
                else:
                    self.logger.error(f"HTTP error downloading from GitHub: {e}")
                    raise RuntimeError(f"Could not download NeqSim from GitHub: {e}") from e
            except Exception as e:
                last_error = e
                self.logger.error(f"Failed to download from GitHub: {e}")
                continue

        error_msg = f"Could not download NeqSim from GitHub for Java {java_version}: {last_error}"
        self.logger.error(error_msg)
        raise RuntimeError(error_msg) from last_error


    def resolve_dependency(self, version: Optional[str] = None, java_version: Optional[int] = None) -> Path:
        # 1. Use specified version or config version
        version = self._resolve_version(version)
        java_version = self._resolve_java_version(java_version)

        # 2. Check for cached JAR
        jar_path = self._get_cached_jar(version, java_version)
        if jar_path:
            self.logger.info(f"Using cached JAR: {jar_path}")
            return jar_path

        # 3. Try to download the JAR for the desired version
        try:
            jar_path = self._get_from_github(version, java_version)
            return jar_path
        except Exception as e:
            self.logger.warning(f"Failed to download JAR for version {version}: {e}")

        # 4. Try fallback version if configured
        fallback = self.config["neqsim"].get("fallback_version")
        if fallback:
            self.logger.info(f"Trying fallback version: {fallback}")
            jar_path = self._get_cached_jar(fallback, java_version)
            if jar_path:
                self.logger.info(f"Using cached fallback JAR: {jar_path}")
                return jar_path
            try:
                jar_path = self._get_from_github(fallback, java_version)
                return jar_path
            except Exception as e:
                self.logger.error(f"Failed to download fallback JAR: {e}")

        # 5. If all fails, raise an error
        raise RuntimeError("Could not resolve or download any NeqSim JAR for your Java version.")

    def _resolve_version(self, version: Optional[str]) -> str:
        # Use the passed version, or the one in config
        if version is not None:
            return version
        version = self.config["neqsim"]["version"]
        if not version:
            raise RuntimeError("No NeqSim version specified in config or arguments.")
        return version

    def _get_cached_jar(self, version: str, java_version: int) -> Optional[Path]:
        for pattern in self._get_jar_patterns(java_version):
            jar_filename = pattern.format(version=version)
            cached_jar = self.jar_cache_dir / jar_filename
            if cached_jar.exists():
                return cached_jar
        return None


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
