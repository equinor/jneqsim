"""
NeqSim Dependency Manager

Handles resolution and downloading of NeqSim Java dependencies from GitHub releases.
"""

import json
import logging
import urllib.request
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import yaml


class NeqSimDependencyManager:
    """Manages NeqSim JAR dependencies from GitHub releases"""

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize dependency manager

        Args:
            config_path: Path to dependencies.yaml, defaults to package config
        """
        if config_path is None:
            config_path = Path(__file__).parent / "dependencies.yaml"

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

    def _validate_url(self, url: str, allowed_hosts: set[str]) -> None:
        """
        Validate URL for security - ensures HTTPS and trusted hosts only

        Args:
            url: URL to validate
            allowed_hosts: Set of allowed hostnames

        Raises:
            ValueError: If URL is invalid or from untrusted host
        """
        parsed = urlparse(url)

        if parsed.scheme != "https":
            raise ValueError(f"Only HTTPS URLs are allowed, got: {parsed.scheme}")

        if parsed.hostname not in allowed_hosts:
            raise ValueError(f"Untrusted host: {parsed.hostname}. Allowed hosts: {allowed_hosts}")

    def get_latest_version(self) -> str:
        """Get latest NeqSim version from GitHub API"""
        repo = self.config["neqsim"]["sources"]["github"]["repository"]
        url = f"https://api.github.com/repos/{repo}/releases/latest"

        # Validate URL for security
        self._validate_url(url, {"api.github.com"})

        try:
            with urllib.request.urlopen(url) as response:  # noqa: S310
                data = json.loads(response.read())
                version = data["tag_name"].lstrip("v")
                self.logger.debug(f"Latest version: {version}")
                return version
        except Exception as e:
            self.logger.error(f"Failed to get latest version: {e}")
            raise RuntimeError(f"Could not determine latest NeqSim version: {e}") from e

    def _download_from_github(self, version: str, java_version: int) -> Path:
        """Download JAR from GitHub releases"""
        github_config = self.config["neqsim"]["sources"]["github"]

        # Determine which JAR to download based on Java version
        if java_version == 8:
            asset_pattern = github_config["assets"]["java8"]
        elif java_version >= 21:
            asset_pattern = github_config["assets"]["java21"]
        else:
            asset_pattern = github_config["assets"]["java11"]

        jar_filename = asset_pattern.format(version=version)
        url = f"{github_config['base_url']}/v{version}/{jar_filename}"

        # Validate URL for security
        self._validate_url(url, {"github.com"})

        # Create temporary file to download to
        import tempfile

        temp_dir = Path(tempfile.mkdtemp(prefix="jneqsim_"))
        downloaded_jar = temp_dir / jar_filename

        try:
            if self.config["logging"]["show_progress"]:
                self.logger.info(f"Downloading {jar_filename} for Java {java_version}...")

            with urllib.request.urlopen(url) as response:  # noqa: S310
                content = response.read()

            downloaded_jar.write_bytes(content)
            self.logger.info(f"Downloaded from GitHub: {downloaded_jar.name}")
            return downloaded_jar

        except Exception as e:
            self.logger.error(f"Failed to download from GitHub: {e}")
            raise RuntimeError(f"Could not download NeqSim from GitHub: {e}") from e

    def resolve_dependency(self, version: Optional[str] = None, java_version: Optional[int] = None) -> Path:
        """
        Resolve NeqSim dependency

        Args:
            version: NeqSim version, defaults to config or latest
            java_version: Java version, auto-detected if None

        Returns:
            Path to resolved JAR file
        """
        # Determine version and java version
        version = self._resolve_version(version)
        java_version = self._resolve_java_version(java_version)

        # Download dependency
        jar_path = self._download_from_github(version, java_version)

        return jar_path

    def _resolve_version(self, version: Optional[str]) -> str:
        """Resolve the NeqSim version to use"""
        if version is None:
            version = self.config["neqsim"]["version"]
            if version == "latest":
                version = self.get_latest_version()

        if version is None:
            raise RuntimeError("Could not determine NeqSim version")

        return version

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
