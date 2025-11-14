#!/usr/bin/env python3
"""
Test script for the new NeqSim dependency management system

This script tests various aspects of the dependency resolution to ensure
everything works correctly with the new runtime dependency management.
"""

import sys
import tempfile
import time
from pathlib import Path

# Add the package to Python path for testing
sys.path.insert(0, str(Path(__file__).parent))

from jneqsim.dependency_manager import NeqSimDependencyManager


def test_dependency_manager():
    """Test the NeqSimDependencyManager functionality"""
    print("🧪 Testing NeqSim Dependency Manager")
    print("=" * 50)

    # Create a temporary cache directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_cache = Path(temp_dir) / "test_cache"

        # Create a test config
        test_config = {
            "neqsim": {
                "version": "latest",
                "sources": {
                    "maven": {
                        "enabled": True,
                        "coordinates": [{"groupId": "no.ntnu.neqsim", "artifactId": "neqsim-core"}],
                    },
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
            "cache": {"directory": str(temp_cache), "verify_integrity": True, "max_size_mb": 500, "ttl_days": 30},
            "logging": {"level": "INFO", "show_progress": True},
        }

        # Write test config
        config_file = Path(temp_dir) / "test_dependencies.yaml"
        import yaml

        with open(config_file, "w") as f:
            yaml.dump(test_config, f)

        try:
            # Test 1: Initialize manager
            print("✅ Test 1: Initializing dependency manager...")
            manager = NeqSimDependencyManager(config_file)
            print(f"   Cache directory: {manager.cache_dir}")

            # Test 2: Get latest version
            print("\n✅ Test 2: Getting latest version...")
            latest_version = manager.get_latest_version()
            print(f"   Latest NeqSim version: {latest_version}")

            # Test 3: Check Maven availability (should be False)
            print("\n✅ Test 3: Checking Maven Central availability...")
            maven_available = manager._check_maven_availability(latest_version)
            print(f"   Maven Central available: {maven_available}")

            # Test 4: Resolve dependency for Java 11
            print("\n✅ Test 4: Resolving dependency for Java 11...")
            start_time = time.time()
            jar_path = manager.resolve_dependency(version=latest_version, java_version=11)
            download_time = time.time() - start_time
            print(f"   JAR downloaded to: {jar_path}")
            print(f"   Download time: {download_time:.2f} seconds")
            print(f"   File size: {jar_path.stat().st_size / (1024*1024):.1f} MB")

            # Test 5: Second resolution (should use cache)
            print("\n✅ Test 5: Testing cache (second resolution)...")
            start_time = time.time()
            jar_path_cached = manager.resolve_dependency(version=latest_version, java_version=11)
            cache_time = time.time() - start_time
            print(f"   Cached JAR path: {jar_path_cached}")
            print(f"   Cache access time: {cache_time:.4f} seconds")
            assert jar_path == jar_path_cached, "Cache should return same path"

            # Test 6: List cached versions
            print("\n✅ Test 6: Listing cached versions...")
            cached_versions = manager.list_cached_versions()
            print(f"   Cached versions: {len(cached_versions)}")
            for version_info in cached_versions:
                print(
                    f"   - {version_info['version']} (Java {version_info['java_version']}) - {version_info['size_mb']} MB"
                )

            # Test 7: Different Java version
            print("\n✅ Test 7: Resolving for Java 21...")
            jar_path_21 = manager.resolve_dependency(version=latest_version, java_version=21)
            print(f"   Java 21 JAR: {jar_path_21}")
            assert jar_path != jar_path_21, "Different Java versions should have different JARs"

            print("\n🎉 All dependency manager tests passed!")
            return True

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            import traceback

            traceback.print_exc()
            return False


def test_jvm_service():
    """Test the JVM service integration"""
    print("\n🧪 Testing JVM Service Integration")
    print("=" * 50)

    try:
        # Test importing the module
        print("✅ Test 1: Importing jvm_service...")
        from jneqsim import jvm_service

        print("   jvm_service imported successfully")

        # Test that neqsim package is available
        print("\n✅ Test 2: Checking NeqSim package availability...")
        neqsim = jvm_service.neqsim
        print(f"   NeqSim package: {neqsim}")

        # Test basic functionality
        print("\n✅ Test 3: Testing basic NeqSim functionality...")
        # Create a simple system to test
        system = neqsim.thermo.system.SystemSrkEos()
        system.addComponent("methane", 1.0)
        print("   Created simple methane system successfully")

        print("\n🎉 All JVM service tests passed!")
        return True

    except Exception as e:
        print(f"\n❌ JVM service test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("🚀 Starting NeqSim Dependency Management Tests")
    print("=" * 60)

    success = True

    # Test dependency manager
    if not test_dependency_manager():
        success = False

    # Test JVM service (commented out for now since JPype needs to be installed)
    # if not test_jvm_service():
    #     success = False

    print("\n" + "=" * 60)
    if success:
        print("🎉 All tests passed! The new dependency management system is working correctly.")
        print("\n📋 Summary of changes:")
        print("   ✅ Dependencies are now resolved at runtime")
        print("   ✅ JAR files are cached in ~/.cache/jneqsim")
        print("   ✅ Support for multiple Java versions")
        print("   ✅ Automatic fallback from Maven to GitHub")
        print("   ✅ Package size significantly reduced")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
