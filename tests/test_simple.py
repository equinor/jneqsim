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
    try:
        print("Testing basic dependency resolution...")

        from jneqsim.dependency_manager import NeqSimDependencyManager

        # Create manager
        manager = NeqSimDependencyManager()

        # Get latest version
        print("Getting latest NeqSim version...")
        latest_version = manager.get_latest_version()
        print(f"Latest version: {latest_version}")

        # Try to resolve for Java 11
        print("Resolving dependency for Java 11...")
        jar_path = manager.resolve_dependency(version=latest_version, java_version=11)
        print(f"✅ Successfully resolved: {jar_path}")
        print(f"   File exists: {jar_path.exists()}")
        print(f"   File size: {jar_path.stat().st_size / (1024*1024):.1f} MB")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_basic_resolution()
    if success:
        print("\n🎉 Basic dependency resolution test passed!")
    else:
        print("\n❌ Test failed!")
    exit(0 if success else 1)
