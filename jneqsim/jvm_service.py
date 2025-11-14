"""
NeqSim JVM Service with enhanced dependency management

This module handles JVM initialization and NeqSim dependency resolution
using the NeqSimDependencyManager for runtime dependency management.
"""

try:
    import jpype

    JPYPE_AVAILABLE = True
except ImportError:
    JPYPE_AVAILABLE = False
    jpype = None

from .dependency_manager import NeqSimDependencyManager


def get_neqsim_jar_path(version: tuple[int, ...]) -> str:
    """
    Get NeqSim JAR path using enhanced dependency resolution

    Args:
        version: JVM version tuple (major, minor, patch)

    Returns:
        Path to NeqSim JAR file

    Raises:
        RuntimeError: If dependency resolution fails
    """
    try:
        manager = NeqSimDependencyManager()
        jar_path = manager.resolve_dependency(java_version=version[0])
        return str(jar_path)
    except Exception as e:
        raise RuntimeError(
            f"Failed to resolve NeqSim dependency for Java {version[0]}.{version[1]}.{version[2]}: {e}"
        ) from e


# Initialize JVM with enhanced dependency resolution (only if JPype is available)
if JPYPE_AVAILABLE and jpype and not jpype.isJVMStarted():
    jpype.startJVM()
    jar_path = get_neqsim_jar_path(jpype.getJVMVersion())
    jpype.addClassPath(jar_path)

if JPYPE_AVAILABLE:
    import jpype.imports

    # This is the java package, added to the python scope by "jpype.imports"
    neqsim = jpype.JPackage("neqsim")
else:
    # Placeholder when JPype is not available (for testing/development)
    neqsim = None
