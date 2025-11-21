"""
Unit tests for JAR caching functionality.
"""

import tempfile
import zipfile
from pathlib import Path

import pytest
import yaml

from jneqsim.dependency_manager import NeqSimDependencyManager


@pytest.fixture
def temp_cache_dir():
    """Create a temporary cache directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir) / "cache"


@pytest.fixture
def temp_work_dir():
    """Create a temporary working directory for test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def sample_jar(temp_work_dir):
    """Create a sample valid JAR file for testing."""
    jar_path = temp_work_dir / "sample.jar"
    with zipfile.ZipFile(jar_path, "w") as zf:
        zf.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
        zf.writestr("test/Sample.class", b"fake class content")
    return jar_path


class TestJARCaching:
    """Test cases for JAR caching functionality."""

    def test_jar_integrity_verification_valid_jar(self, temp_cache_dir, sample_jar):
        """Test JAR integrity verification with valid JAR."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Test valid JAR
        assert cache_manager._verify_jar_integrity(sample_jar)

    def test_jar_integrity_verification_invalid_jar(self, temp_cache_dir, temp_work_dir):
        """Test JAR integrity verification with invalid JAR."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Test invalid JAR (corrupted file)
        corrupt_jar = temp_work_dir / "corrupt.jar"
        corrupt_jar.write_text("not a valid jar file")
        assert not cache_manager._verify_jar_integrity(corrupt_jar)

        # Test non-existent file
        fake_jar = temp_work_dir / "fake.jar"
        assert not cache_manager._verify_jar_integrity(fake_jar)

    def test_cached_jar_lookup_miss(self, temp_cache_dir):
        """Test cached JAR lookup when no cached JAR exists."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Test cache miss - no cached JAR
        result = cache_manager.get_cached_jar("3.1.2", 11)
        assert result is None

    def test_cached_jar_lookup_hit(self, temp_cache_dir, sample_jar):
        """Test cached JAR lookup when cached JAR exists."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Cache the JAR
        cached_jar = cache_manager.cache_jar(sample_jar, "3.1.2", 11)
        assert cached_jar.exists()

        # Test cache hit
        result = cache_manager.get_cached_jar("3.1.2", 11)
        assert result is not None
        assert result == cached_jar

    def test_cache_filename_generation(self, temp_cache_dir):
        """Test cache filename generation."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Test filename generation
        filename1 = cache_manager._get_cache_filename("3.1.2", 11)
        filename2 = cache_manager._get_cache_filename("3.1.2", 21)
        filename3 = cache_manager._get_cache_filename("3.0.0", 11)

        # Different versions/java versions should have different filenames
        assert filename1 != filename2
        assert filename1 != filename3

        # Filenames should follow expected pattern
        assert filename1 == "neqsim-3.1.2-java11.jar"
        assert filename2 == "neqsim-3.1.2-java21.jar"
        assert filename3 == "neqsim-3.0.0-java11.jar"

    def test_cache_replacement(self, temp_cache_dir, temp_work_dir):
        """Test that caching replaces existing cached JARs."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Create first JAR
        test_jar1 = temp_work_dir / "neqsim-3.1.2-v1.jar"
        with zipfile.ZipFile(test_jar1, "w") as zf:
            zf.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
            zf.writestr("version.txt", "version 1")

        # Cache first version
        cached_jar1 = cache_manager.cache_jar(test_jar1, "3.1.2", 11)
        assert cached_jar1.exists()

        # Create second JAR with same version/java version
        test_jar2 = temp_work_dir / "neqsim-3.1.2-v2.jar"
        with zipfile.ZipFile(test_jar2, "w") as zf:
            zf.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
            zf.writestr("version.txt", "version 2")

        # Cache second version (should replace first)
        cached_jar2 = cache_manager.cache_jar(test_jar2, "3.1.2", 11)

        # Should be same location
        assert cached_jar1 == cached_jar2

        # Should contain content from second JAR
        with zipfile.ZipFile(cached_jar2, "r") as zf:
            version_content = zf.read("version.txt").decode()
            assert version_content == "version 2"

    def test_cache_disabled_behavior(self, temp_cache_dir, temp_work_dir):
        """Test behavior when caching is disabled."""
        # Create a custom config with caching disabled
        config = {
            "neqsim": {
                "version": "3.1.2",
                "fallback_version": "3.1.1",
                "sources": {
                    "github": {
                        "repository": "equinor/neqsim",
                        "base_url": "https://github.com/equinor/neqsim/releases/download",
                        "assets": {
                            "java8": "neqsim-{version}-Java8.jar",
                            "java11": "neqsim-{version}.jar",
                            "java21": "neqsim-{version}-Java21.jar",
                        },
                    }
                },
            },
            "logging": {"level": "INFO", "show_progress": True},
            "cache": {"enabled": False, "verify_integrity": True},
        }

        config_file = temp_work_dir / "config.yaml"
        with open(config_file, "w") as f:
            yaml.dump(config, f)

        manager = NeqSimDependencyManager(config_path=config_file, cache_dir=temp_cache_dir)
        cache_manager = manager.cache_manager

        # Test that get_cached_jar returns None when caching is disabled
        result = cache_manager.get_cached_jar("3.1.2", 11)
        assert result is None

        # Test that cache_jar returns the source jar when caching is disabled
        test_jar = temp_work_dir / "test.jar"
        with zipfile.ZipFile(test_jar, "w") as zf:
            zf.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")

        result_jar = cache_manager.cache_jar(test_jar, "3.1.2", 11)
        assert result_jar == test_jar  # Should return original

    def test_cache_directory_creation(self, temp_work_dir):
        """Test that cache directory is created automatically."""
        cache_dir = temp_work_dir / "new_cache"
        assert not cache_dir.exists()

        # Initialize manager with non-existent cache directory
        manager = NeqSimDependencyManager(cache_dir=cache_dir)

        # Cache directory should be created
        assert cache_dir.exists()
        assert manager.cache_dir == cache_dir

    @pytest.mark.unit
    def test_cache_manager_initialization(self, temp_cache_dir):
        """Test that cache manager initializes correctly."""
        manager = NeqSimDependencyManager(cache_dir=temp_cache_dir)

        assert manager.cache_manager is not None
        assert manager.cache_manager.cache_dir == temp_cache_dir


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
