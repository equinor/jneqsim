#!/usr/bin/env python3
"""
Simple test to verify the dependency manager can resolve NeqSim JARs
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))


def test_basic_resolution():
    """Test basic dependency resolution without JVM"""
    print("Testing basic dependency resolution...")

    from jneqsim.dependency_manager import NeqSimDependencyManager

    # Create manager
    manager = NeqSimDependencyManager()

    # Get latest version
    print("Getting latest NeqSim version...")
    latest_version = manager.config["neqsim"]["version"]
    print(f"Latest version: {latest_version}")
    assert latest_version is not None, "Failed to get latest version"

    # Try to resolve for Java 11
    print("Resolving dependency for Java 11...")
    jar_path = manager.resolve_dependency(version=latest_version, java_version=11)
    print(f"✅ Successfully resolved: {jar_path}")

    # Assertions
    assert jar_path is not None, "Failed to resolve JAR path"
    assert jar_path.exists(), f"JAR file does not exist: {jar_path}"

    file_size_mb = jar_path.stat().st_size / (1024 * 1024)
    print(f"   File exists: {jar_path.exists()}")
    print(f"   File size: {file_size_mb:.1f} MB")
    assert file_size_mb > 0, "JAR file is empty"


if __name__ == "__main__":
    success = test_basic_resolution()
    if success:
        print("\n🎉 Basic dependency resolution test passed!")
    else:
        print("\n❌ Test failed!")
    exit(0 if success else 1)
