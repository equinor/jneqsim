"""
NeqSim Dependency Manager

Handles resolution, downloading, and caching of NeqSim Java dependencies
with support for both Maven Central and GitHub releases.
"""

import hashlib
import json
import logging
import shutil
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional

import yaml


class NeqSimDependencyManager:
    """Manages NeqSim JAR dependencies with Maven and GitHub support"""

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize dependency manager

        Args:
            config_path: Path to dependencies.yaml, defaults to package config
        """
        if config_path is None:
            config_path = Path(__file__).parent / "dependencies.yaml"

        self.config = self._load_config(config_path)
        self.cache_dir = Path(self.config["cache"]["directory"]).expanduser()
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.manifest_path = self.cache_dir / "manifest.json"
        self.logger = self._setup_logging()

        # Clean up old cache entries
        self._cleanup_cache()

    def _load_config(self, config_path: Path) -> Dict:
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

    def _get_manifest(self) -> Dict:
        """Load cached dependency manifest"""
        if self.manifest_path.exists():
            try:
                return json.loads(self.manifest_path.read_text())
            except (json.JSONDecodeError, OSError) as e:
                self.logger.warning(f"Failed to load manifest: {e}")
        return {}

    def _save_manifest(self, manifest: Dict):
        """Save dependency manifest"""
        try:
            self.manifest_path.write_text(json.dumps(manifest, indent=2))
        except OSError as e:
            self.logger.error(f"Failed to save manifest: {e}")

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file"""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    def _cleanup_cache(self):
        """Clean up old cache entries based on TTL and size limits"""
        manifest = self._get_manifest()
        ttl_days = self.config["cache"]["ttl_days"]
        max_size_mb = self.config["cache"]["max_size_mb"]

        if ttl_days <= 0 and max_size_mb <= 0:
            return

        current_time = time.time()
        files_to_remove = []

        # Check TTL
        if ttl_days > 0:
            ttl_seconds = ttl_days * 24 * 60 * 60
            for key, entry in manifest.items():
                if "timestamp" in entry:
                    if current_time - entry["timestamp"] > ttl_seconds:
                        files_to_remove.append(key)

        # Check size limits
        if max_size_mb > 0:
            cache_files = [
                (p, p.stat().st_size, p.stat().st_mtime) for p in self.cache_dir.glob("*.jar") if p.is_file()
            ]
            total_size = sum(size for _, size, _ in cache_files)

            if total_size > max_size_mb * 1024 * 1024:
                # Sort by modification time, oldest first
                cache_files.sort(key=lambda x: x[2])

                for file_path, size, _ in cache_files:
                    if total_size <= max_size_mb * 1024 * 1024:
                        break

                    # Find manifest key for this file
                    for key, entry in manifest.items():
                        if entry.get("path") == str(file_path):
                            files_to_remove.append(key)
                            break

                    total_size -= size

        # Remove files
        for key in files_to_remove:
            if key in manifest:
                file_path = Path(manifest[key]["path"])
                if file_path.exists():
                    try:
                        file_path.unlink()
                        self.logger.info(f"Removed cached file: {file_path.name}")
                    except OSError as e:
                        self.logger.warning(f"Failed to remove {file_path}: {e}")
                del manifest[key]

        if files_to_remove:
            self._save_manifest(manifest)

    def get_latest_version(self) -> str:
        """Get latest NeqSim version from GitHub API"""
        repo = self.config["neqsim"]["sources"]["github"]["repository"]
        url = f"https://api.github.com/repos/{repo}/releases/latest"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())
                version = data["tag_name"].lstrip("v")
                self.logger.debug(f"Latest version: {version}")
                return version
        except Exception as e:
            self.logger.error(f"Failed to get latest version: {e}")
            raise RuntimeError(f"Could not determine latest NeqSim version: {e}")

    def _check_maven_availability(self, version: str) -> bool:
        """Check if NeqSim is available in Maven Central"""
        if not self.config["neqsim"]["sources"]["maven"]["enabled"]:
            return False

        coords = self.config["neqsim"]["sources"]["maven"]["coordinates"][0]
        search_url = (
            f"https://search.maven.org/solrsearch/select?"
            f"q=g:{coords['groupId']}+AND+a:{coords['artifactId']}+AND+v:{version}&wt=json"
        )

        try:
            with urllib.request.urlopen(search_url) as response:
                data = json.loads(response.read())
                available = data["response"]["numFound"] > 0
                self.logger.debug(f"Maven availability for {version}: {available}")
                return available
        except Exception as e:
            self.logger.debug(f"Maven check failed: {e}")
            return False

    def _download_from_maven(self, version: str) -> Path:
        """Download JAR using Maven dependency resolution"""
        coords = self.config["neqsim"]["sources"]["maven"]["coordinates"][0]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create minimal pom.xml
            pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.temp</groupId>
    <artifactId>neqsim-resolver</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>{coords['groupId']}</groupId>
            <artifactId>{coords['artifactId']}</artifactId>
            <version>{version}</version>
        </dependency>
    </dependencies>
</project>"""

            pom_path = temp_path / "pom.xml"
            pom_path.write_text(pom_content)

            # Use Maven to download dependencies
            result = subprocess.run(
                [
                    "mvn",
                    "dependency:copy-dependencies",
                    "-DoutputDirectory=target/lib",
                    "-DincludeScope=runtime",
                    "-f",
                    str(pom_path),
                ],
                cwd=temp_path,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                raise RuntimeError(f"Maven download failed: {result.stderr}")

            # Find the NeqSim JAR
            lib_dir = temp_path / "target" / "lib"
            jar_files = list(lib_dir.glob("neqsim*.jar"))

            if not jar_files:
                raise RuntimeError("No NeqSim JAR found in Maven download")

            # Copy to cache
            cached_jar = self.cache_dir / f"neqsim-{version}-maven.jar"
            shutil.copy2(jar_files[0], cached_jar)

            self.logger.info(f"Downloaded from Maven: {cached_jar.name}")
            return cached_jar

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

        cached_jar = self.cache_dir / f"neqsim-{version}-java{java_version}.jar"

        try:
            if self.config["logging"]["show_progress"]:
                self.logger.info(f"Downloading {jar_filename} for Java {java_version}...")

            with urllib.request.urlopen(url) as response:
                content = response.read()

            cached_jar.write_bytes(content)
            self.logger.info(f"Downloaded from GitHub: {cached_jar.name}")
            return cached_jar

        except Exception as e:
            self.logger.error(f"Failed to download from GitHub: {e}")
            raise RuntimeError(f"Could not download NeqSim from GitHub: {e}")

    def resolve_dependency(self, version: Optional[str] = None, java_version: Optional[int] = None) -> Path:
        """
        Resolve NeqSim dependency

        Args:
            version: NeqSim version, defaults to config or latest
            java_version: Java version, auto-detected if None

        Returns:
            Path to resolved JAR file
        """
        # Determine version
        if version is None:
            version = self.config["neqsim"]["version"]
            if version == "latest":
                version = self.get_latest_version()

        # Ensure version is not None
        if version is None:
            raise RuntimeError("Could not determine NeqSim version")

        # Auto-detect Java version if needed
        if java_version is None:
            try:
                import jpype

                if jpype.isJVMStarted():
                    java_version = jpype.getJVMVersion()[0]
                else:
                    java_version = 11  # Default fallback
            except ImportError:
                java_version = 11  # Default fallback

        # Ensure java_version is not None
        if java_version is None:
            java_version = 11

        # Check cache first
        cache_key = f"{version}-java{java_version}"
        manifest = self._get_manifest()

        if cache_key in manifest:
            cached_path = Path(manifest[cache_key]["path"])
            if cached_path.exists():
                # Verify integrity if enabled
                if self.config["cache"]["verify_integrity"]:
                    current_hash = self._calculate_file_hash(cached_path)
                    if current_hash == manifest[cache_key]["hash"]:
                        self.logger.debug(f"Using cached JAR: {cached_path.name}")
                        return cached_path
                    else:
                        self.logger.warning(f"Cache integrity check failed for {cached_path.name}")
                else:
                    self.logger.debug(f"Using cached JAR: {cached_path.name}")
                    return cached_path

        # Try Maven Central first
        jar_path = None
        if self._check_maven_availability(version):
            try:
                jar_path = self._download_from_maven(version)
                cache_key = f"{version}-maven"  # Different key for Maven downloads
            except Exception as e:
                self.logger.warning(f"Maven download failed, falling back to GitHub: {e}")

        # Fall back to GitHub
        if jar_path is None:
            jar_path = self._download_from_github(version, java_version)

        # Update cache manifest
        file_hash = self._calculate_file_hash(jar_path)
        manifest[cache_key] = {
            "path": str(jar_path),
            "version": version,
            "java_version": java_version,
            "hash": file_hash,
            "timestamp": time.time(),
            "source": "maven" if "maven" in cache_key else "github",
        }
        self._save_manifest(manifest)

        return jar_path

    def clear_cache(self):
        """Clear all cached dependencies"""
        try:
            for jar_file in self.cache_dir.glob("*.jar"):
                jar_file.unlink()
            if self.manifest_path.exists():
                self.manifest_path.unlink()
            self.logger.info("Cache cleared")
        except Exception as e:
            self.logger.error(f"Failed to clear cache: {e}")

    def list_cached_versions(self) -> List[Dict]:
        """List all cached versions"""
        manifest = self._get_manifest()
        return [
            {
                "version": entry["version"],
                "java_version": entry.get("java_version"),
                "source": entry.get("source", "unknown"),
                "path": entry["path"],
                "size_mb": round(Path(entry["path"]).stat().st_size / (1024 * 1024), 2),
            }
            for entry in manifest.values()
            if Path(entry["path"]).exists()
        ]
