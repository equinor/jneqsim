try:
    import jpype

    JPYPE_AVAILABLE = True
except ImportError:
    JPYPE_AVAILABLE = False
    jpype = None

from .dependency_manager import NeqSimDependencyManager


def get_neqsim_jar_path(java_version: tuple[int, ...]) -> str:
    """
    Get NeqSim JAR path using enhanced dependency resolution

    Args:
        java_version: JVM version tuple (major, minor, patch)

    Returns:
        Path to NeqSim JAR file

    Raises:
        RuntimeError: If dependency resolution fails
    """
    try:
        manager = NeqSimDependencyManager()
        if all(v == 0 for v in java_version):
            java_version = (11,)
        jar_path = manager.resolve_dependency(java_version=java_version[0])
        return str(jar_path)
    except Exception as e:
        raise RuntimeError(
            f"Failed to resolve NeqSim dependency for Java {'.'.join(map(str, java_version))}: {e}"
        ) from e


# Initialize JVM and NeqSim package
neqsim = None  # Default to None, cannot use NeqSim if JVM fails to start

if JPYPE_AVAILABLE and jpype and not jpype.isJVMStarted():
    # We need to start the JVM before importing the neqsim package
    try:
        jar_path = get_neqsim_jar_path(jpype.getJVMVersion())
        jpype.startJVM(classpath=[jar_path])

        import jpype.imports

        # This is the java package, added to the python scope by "jpype.imports"
        neqsim = jpype.JPackage("neqsim")
    except Exception as e:
        # JVM Start failed, handle gracefully
        import warnings

        warnings.warn(f"Failed to initialize JVM: {e}. NeqSim functionality will not be available.", stacklevel=2)
elif JPYPE_AVAILABLE and jpype and jpype.isJVMStarted():
    # JVM already started, just get the package
    import jpype.imports

    neqsim = jpype.JPackage("neqsim")
