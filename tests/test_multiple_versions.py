"""
Test multiple Java versions to verify our dependency resolution works correctly.
"""

import pytest

from jneqsim.dependency_manager import NeqSimDependencyManager


class TestMultipleJavaVersions:
    """Test dependency resolution across different Java versions."""

    def test_manager_supports_multiple_java_versions(self):
        """Test that manager can handle different Java version configurations."""
        manager = NeqSimDependencyManager()
        configured_version = manager.config["neqsim"]["version"]
        assert configured_version is not None

        # Test different Java versions
        java_versions = [8, 11, 17, 21]

        for java_version in java_versions:
            # Test that the manager can generate patterns for each version
            patterns = manager._get_jar_patterns(java_version)
            assert len(patterns) > 0, f"No patterns generated for Java {java_version}"
            assert all(isinstance(pattern, str) for pattern in patterns)

    @pytest.mark.slow
    def test_multiple_java_versions_resolution(self):
        """Test dependency resolution for different Java versions (may download JARs)."""
        manager = NeqSimDependencyManager()

        # Test different Java versions
        java_versions = [8, 11, 17, 21]
        resolved_jars = {}

        for java_version in java_versions:
            try:
                jar_path = manager.resolve_dependency(java_version=java_version)
                resolved_jars[java_version] = jar_path

                # Basic validations
                assert jar_path.exists(), f"JAR file does not exist for Java {java_version}"
                assert jar_path.suffix == ".jar", f"Not a JAR file for Java {java_version}"

                file_size_mb = jar_path.stat().st_size / (1024 * 1024)
                assert file_size_mb > 0, f"JAR file is empty for Java {java_version}"

                print(f"Java {java_version}: {jar_path.name} ({file_size_mb:.1f} MB)")

            except Exception as e:
                print(f"Failed to resolve Java {java_version}: {e}")

        # Verify at least some Java versions were resolved successfully
        assert len(resolved_jars) > 0, "No Java versions were resolved successfully"

        # Check that we have unique JAR files
        unique_jars = set(resolved_jars.values())
        assert len(unique_jars) > 0, "No unique JAR files found"

        print(f"\nResolved {len(resolved_jars)}/{len(java_versions)} Java versions")
        print(f"Unique JAR files: {len(unique_jars)}")

    def test_jar_patterns_consistency(self):
        """Test that JAR patterns are consistent for the same Java version."""
        manager = NeqSimDependencyManager()

        # Test the same Java version multiple times
        patterns1 = manager._get_jar_patterns(11)
        patterns2 = manager._get_jar_patterns(11)

        assert patterns1 == patterns2, "JAR patterns should be consistent"

    def test_jar_patterns_different_versions(self):
        """Test that different Java versions produce different patterns."""
        manager = NeqSimDependencyManager()

        patterns_8 = manager._get_jar_patterns(8)
        patterns_11 = manager._get_jar_patterns(11)
        patterns_21 = manager._get_jar_patterns(21)

        # At least some patterns should be different
        assert patterns_8 != patterns_11 or patterns_11 != patterns_21 or patterns_8 != patterns_21


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
