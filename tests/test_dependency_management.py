import tempfile
import time
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from jneqsim.dependency_manager import NeqSimDependencyManager


@pytest.fixture
def test_config():
    """Fixture providing test configuration for dependency manager."""
    return {
        "neqsim": {
            "version": "3.1.2",
            "fallback_version": "3.1.1",
            "sources": {
                "github": {
                    "enabled": True,
                    "repository": "equinor/neqsim",
                    "base_url": "https://github.com/equinor/neqsim/releases/download",
                    "assets": {
                        "java8": "neqsim-{version}-Java8.jar",
                        "java11": "neqsim-{version}.jar",
                        "java21": "neqsim-{version}-Java21.jar",
                    },
                },
            },
        },
        "logging": {"level": "INFO", "show_progress": True},
    }


@pytest.fixture
def temp_config_file(test_config):
    """Fixture that creates a temporary config file for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_file = Path(temp_dir) / "test_dependencies.yaml"
        with open(config_file, "w") as f:
            yaml.dump(test_config, f)
        yield config_file


@pytest.fixture
def temp_cache_dir():
    """Fixture that creates a temporary cache directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir) / "cache"


class TestNeqSimDependencyManager:
    """Test cases for NeqSimDependencyManager."""

    def test_initialization_with_default_config(self):
        """Test initializing dependency manager with default configuration."""
        manager = NeqSimDependencyManager()

        assert manager.config is not None
        assert "neqsim" in manager.config
        assert "version" in manager.config["neqsim"]
        assert manager.logger is not None
        assert manager.cache_manager is not None

    def test_initialization_with_custom_config(self, temp_config_file, temp_cache_dir):
        """Test initializing dependency manager with custom configuration."""
        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        assert manager.config["neqsim"]["version"] == "3.1.2"
        assert manager.config["neqsim"]["fallback_version"] == "3.1.1"
        assert manager.cache_dir == temp_cache_dir

    def test_get_configured_version(self, temp_config_file, temp_cache_dir):
        """Test getting the configured NeqSim version."""
        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        configured_version = manager.config["neqsim"]["version"]
        assert configured_version == "3.1.2"

    def test_jar_patterns_java8(self, temp_config_file, temp_cache_dir):
        """Test JAR filename patterns for Java 8."""
        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        patterns = manager._get_jar_patterns(8)
        expected_patterns = [
            "neqsim-{version}-Java8-Java8.jar",
            "neqsim-{version}-Java8.jar",
            "neqsim-{version}.jar",
        ]
        assert patterns == expected_patterns

    def test_jar_patterns_java11(self, temp_config_file, temp_cache_dir):
        """Test JAR filename patterns for Java 11."""
        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        patterns = manager._get_jar_patterns(11)
        expected_patterns = [
            "neqsim-{version}.jar",
            "neqsim-{version}.jar",
        ]
        assert patterns == expected_patterns

    def test_jar_patterns_java21(self, temp_config_file, temp_cache_dir):
        """Test JAR filename patterns for Java 21."""
        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        patterns = manager._get_jar_patterns(21)
        expected_patterns = [
            "neqsim-{version}-Java21-Java21.jar",
            "neqsim-{version}-Java21.jar",
            "neqsim-{version}.jar",
        ]
        assert patterns == expected_patterns

    @patch("jneqsim.dependency_manager.NeqSimDependencyManager._get_jar_from_github")
    def test_resolve_dependency_success(self, mock_get_jar_from_github, temp_config_file, temp_cache_dir):
        """Test successful dependency resolution."""
        # Setup mock
        mock_jar_path = Path("/fake/path/neqsim-3.1.2.jar")
        mock_get_jar_from_github.return_value = mock_jar_path

        manager = NeqSimDependencyManager(config_path=temp_config_file, cache_dir=temp_cache_dir)

        # Test resolution
        result = manager.resolve_dependency(java_version=11)

        assert result == mock_jar_path
        mock_get_jar_from_github.assert_called_once_with("3.1.2", 11)

    def test_config_loading_invalid_file(self):
        """Test error handling when loading invalid config file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("invalid: yaml: content: [")
            invalid_config_path = Path(f.name)

        try:
            with pytest.raises(yaml.YAMLError):
                NeqSimDependencyManager(config_path=invalid_config_path)
        finally:
            invalid_config_path.unlink()

    def test_config_loading_missing_file(self):
        """Test error handling when config file is missing."""
        nonexistent_path = Path("/nonexistent/config.yaml")

        with pytest.raises(FileNotFoundError):
            NeqSimDependencyManager(config_path=nonexistent_path)


class TestDependencyResolutionIntegration:
    """Integration tests for dependency resolution (may download real JARs)."""

    @pytest.mark.slow
    def test_resolve_dependency_java11_real(self):
        """Integration test: resolve real dependency for Java 11.

        This test actually downloads a JAR file and may be slow.
        """
        manager = NeqSimDependencyManager()

        start_time = time.time()
        jar_path = manager.resolve_dependency(java_version=11)
        download_time = time.time() - start_time

        # Assertions
        assert jar_path is not None
        assert jar_path.exists()
        assert jar_path.suffix == ".jar"

        file_size_mb = jar_path.stat().st_size / (1024 * 1024)
        assert file_size_mb > 0, "JAR file should not be empty"

        # Log some info for debugging
        print(f"\nJAR downloaded to: {jar_path}")
        print(f"Download time: {download_time:.2f} seconds")
        print(f"File size: {file_size_mb:.1f} MB")

    @pytest.mark.slow
    def test_resolve_dependency_different_java_versions(self):
        """Integration test: resolve dependencies for different Java versions.

        This test actually downloads JAR files and may be slow.
        """
        manager = NeqSimDependencyManager()

        # Test Java 11
        jar_path_11 = manager.resolve_dependency(java_version=11)
        assert jar_path_11.exists()

        # Test Java 21
        jar_path_21 = manager.resolve_dependency(java_version=21)
        assert jar_path_21.exists()

        # Different Java versions may result in different JAR files
        # (though they might be the same if only one version is available)
        print(f"\nJava 11 JAR: {jar_path_11}")
        print(f"Java 21 JAR: {jar_path_21}")

    @pytest.mark.slow
    def test_cache_functionality(self):
        """Integration test: verify caching works correctly."""
        manager = NeqSimDependencyManager()

        # First resolution (may download)
        start_time = time.time()
        jar_path_1 = manager.resolve_dependency(java_version=11)
        first_time = time.time() - start_time

        # Second resolution (should use cache)
        start_time = time.time()
        jar_path_2 = manager.resolve_dependency(java_version=11)
        second_time = time.time() - start_time

        # Should get the same file
        assert jar_path_1 == jar_path_2
        assert jar_path_1.exists()

        # Second call should be faster (cached)
        # Note: This might not always be true due to filesystem caching
        print(f"\nFirst resolution: {first_time:.2f}s")
        print(f"Second resolution: {second_time:.2f}s")


class TestJVMServiceIntegration:
    """Test JVM service integration (optional, requires JPype)."""

    def test_jvm_service_import(self):
        """Test importing jvm_service module."""
        try:
            from jneqsim import jvm_service

            assert jvm_service is not None
        except ImportError as e:
            pytest.skip(f"JPype not available: {e}")

    @pytest.mark.skipif(
        condition=True,  # Skip by default since it requires JPype setup
        reason="Requires JPype installation and may start JVM",
    )
    def test_neqsim_package_availability(self):
        """Test that NeqSim package is available through JVM service.

        This test is skipped by default as it requires JPype and may start the JVM.
        """
        try:
            from jneqsim import jvm_service

            # Check if NeqSim is available
            neqsim = jvm_service.neqsim
            if neqsim is not None:
                # Try to create a simple system
                system = neqsim.thermo.system.SystemSrkEos()
                system.addComponent("methane", 1.0)
                assert True  # Test passed if no exception
            else:
                pytest.skip("NeqSim not available through jvm_service")

        except ImportError:
            pytest.skip("JPype not available")
        except Exception as e:
            pytest.fail(f"JVM service test failed: {e}")


if __name__ == "__main__":
    # Allow running tests directly with python
    pytest.main([__file__, "-v"])
