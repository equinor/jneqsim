import pytest

from jneqsim.dependency_manager import NeqSimDependencyManager


@pytest.mark.integration
class TestBasicDependencyResolution:
    """Basic integration tests for dependency resolution."""

    def test_manager_initialization(self):
        """Test that dependency manager initializes correctly."""
        manager = NeqSimDependencyManager()

        assert manager.config is not None
        assert "neqsim" in manager.config
        assert "version" in manager.config["neqsim"]
        assert manager.logger is not None

    def test_configured_version_access(self):
        """Test that we can access the configured NeqSim version."""
        manager = NeqSimDependencyManager()

        configured_version = manager.config["neqsim"]["version"]
        assert configured_version is not None
        assert isinstance(configured_version, str)
        assert len(configured_version) > 0

    @pytest.mark.slow
    def test_basic_resolution_java11(self):
        """Test basic dependency resolution for Java 11 (may download JAR)."""
        manager = NeqSimDependencyManager()

        # Try to resolve for Java 11
        jar_path = manager.resolve_dependency(java_version=11)

        # Assertions
        assert jar_path is not None, "Failed to resolve JAR path"
        assert jar_path.exists(), f"JAR file does not exist: {jar_path}"
        assert jar_path.suffix == ".jar", "Resolved file should be a JAR"

        file_size_mb = jar_path.stat().st_size / (1024 * 1024)
        assert file_size_mb > 0, "JAR file should not be empty"

        # Log some information for debugging
        print(f"\nResolved JAR: {jar_path}")
        print(f"File size: {file_size_mb:.1f} MB")
        print(f"File exists: {jar_path.exists()}")

    @pytest.mark.slow
    def test_resolution_different_java_versions(self):
        """Test that resolution works for different Java versions."""
        manager = NeqSimDependencyManager()

        # Test Java 11
        jar_path_11 = manager.resolve_dependency(java_version=11)
        assert jar_path_11.exists()

        # Test Java 21
        jar_path_21 = manager.resolve_dependency(java_version=21)
        assert jar_path_21.exists()

        # Both should be valid JARs
        assert jar_path_11.suffix == ".jar"
        assert jar_path_21.suffix == ".jar"

        print(f"\nJava 11 JAR: {jar_path_11}")
        print(f"Java 21 JAR: {jar_path_21}")


if __name__ == "__main__":
    exit_code = pytest.main([__file__, "-v"])
    exit(exit_code)
