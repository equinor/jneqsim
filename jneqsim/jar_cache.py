import logging
import shutil
import zipfile
from pathlib import Path
from typing import Optional


class JARCacheManager:
    """Simplified JAR cache manager that caches one JAR per version/java_version combination"""

    def __init__(self, cache_dir: Path, config: dict, logger: logging.Logger):
        """
        Initialize cache manager

        Args:
            cache_dir: Base cache directory
            config: Configuration dictionary
            logger: Logger instance
        """
        self.cache_dir = cache_dir
        self.jar_cache_dir = cache_dir / "jars"
        self.jar_cache_dir.mkdir(parents=True, exist_ok=True)
        self.config = config
        self.logger = logger

    def _get_cache_filename(self, version: str, java_version: int) -> str:
        """Generate simple cache filename for version and Java version combination"""
        return f"neqsim-{version}-java{java_version}.jar"

    def get_cached_jar(self, version: str, java_version: int) -> Optional[Path]:
        """Check if JAR exists in cache for the specified version and Java version"""
        if not self.config.get("cache", {}).get("enabled", True):
            return None

        cache_filename = self._get_cache_filename(version, java_version)
        cached_jar = self.jar_cache_dir / cache_filename

        if not cached_jar.exists():
            self.logger.debug(f"No cached JAR found for version {version}, Java {java_version}")
            return None

        # Verify integrity if enabled
        if self.config.get("cache", {}).get("verify_integrity", True):
            if not self._verify_jar_integrity(cached_jar):
                self.logger.warning(f"Cached JAR failed integrity check, removing: {cached_jar.name}")
                cached_jar.unlink()  # Remove corrupted cache
                return None

        self.logger.info(f"Using cached JAR: {cached_jar.name}")
        return cached_jar

    def cache_jar(self, source_jar: Path, version: str, java_version: int) -> Path:
        """Cache downloaded JAR file, replacing any existing cached version"""
        if not self.config.get("cache", {}).get("enabled", True):
            return source_jar

        cache_filename = self._get_cache_filename(version, java_version)
        cached_jar = self.jar_cache_dir / cache_filename

        # Remove any existing cached JAR for this version/java_version
        if cached_jar.exists():
            cached_jar.unlink()
            self.logger.debug(f"Replaced cached JAR: {cache_filename}")

        # Copy to cache
        shutil.copy2(source_jar, cached_jar)

        self.logger.info(f"Cached JAR: {cached_jar.name}")

        return cached_jar

    def _verify_jar_integrity(self, jar_path: Path) -> bool:
        """Verify JAR file is not corrupted"""
        try:
            # Basic checks: file exists, has content, ends with proper extension
            if not jar_path.exists() or jar_path.stat().st_size == 0:
                return False

            # Check if it's a valid ZIP file (JARs are ZIP files)
            with zipfile.ZipFile(jar_path, "r") as zf:
                # Try to read the file list - this will fail if corrupted
                zf.namelist()
                return True
        except Exception as e:
            self.logger.debug(f"JAR integrity check failed for {jar_path}: {e}")
            return False
