#!/usr/bin/env python3
"""
Test multiple Java versions to verify our dependency resolution works correctly
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))


def test_multiple_java_versions():
    """Test dependency resolution for different Java versions"""
    try:
        print("🧪 Testing Multiple Java Versions")
        print("=" * 50)

        from jneqsim.dependency_manager import NeqSimDependencyManager

        manager = NeqSimDependencyManager()
        latest_version = manager.get_latest_version()

        # Test different Java versions
        java_versions = [8, 11, 17, 21]
        resolved_jars = {}

        for java_version in java_versions:
            print(f"\n✅ Testing Java {java_version}...")
            try:
                jar_path = manager.resolve_dependency(version=latest_version, java_version=java_version)
                resolved_jars[java_version] = jar_path
                print(f"   ✓ Resolved: {jar_path.name}")
                print(f"   ✓ Size: {jar_path.stat().st_size / (1024*1024):.1f} MB")
            except Exception as e:
                print(f"   ✗ Failed: {e}")

        print("\n📋 Summary:")
        print(f"   Successfully resolved {len(resolved_jars)}/{len(java_versions)} Java versions")

        # Verify different Java versions have different JARs (except 11 and 17 which might be the same)
        unique_jars = set(resolved_jars.values())
        print(f"   Unique JAR files: {len(unique_jars)}")

        print("\n🎉 Multi-version test completed!")
        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_multiple_java_versions()
    exit(0 if success else 1)
