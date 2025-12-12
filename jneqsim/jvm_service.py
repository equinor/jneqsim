try:
    import jpype

    JPYPE_AVAILABLE = True
except ImportError:
    JPYPE_AVAILABLE = False
    jpype = None

import logging
from pathlib import Path

from jneqsim.common.load_config import load_config
from jneqsim.common.setup_logging import setup_logging

from .dependency_manager import NeqSimDependencyManager


def get_neqsim_jar_path(java_version: tuple[int, ...], logger: logging.Logger, config: dict) -> str:
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
        manager = NeqSimDependencyManager(logger, config)
        jar_path = manager.resolve_dependency(java_version=java_version[0])
        return str(jar_path)
    except Exception as e:
        raise RuntimeError(
            f"Failed to resolve NeqSim dependency for Java {'.'.join(map(str, java_version))}: {e}"
        ) from e


# Load configuration and setup logging
config_path = Path(__file__).parent / "common" / "config.yaml"
config = load_config(config_path)
logger = setup_logging(config)

# Initialize JVM and NeqSim package
neqsim = None  # Default to None, cannot use NeqSim if JVM fails to start

if JPYPE_AVAILABLE and jpype and not jpype.isJVMStarted():
    # We need to start the JVM before importing the neqsim package
    try:
        jpype.startJVM()
        jar_path = get_neqsim_jar_path(jpype.getJVMVersion(), logger, config)
        jpype.addClassPath(jar_path)

        import jpype.imports

        # This is the java package, added to the python scope by "jpype.imports"
        neqsim = jpype.JPackage("neqsim")
    except Exception as e:
        # JVM Start failed, handle gracefully

        logger.error(f"Failed to initialize JVM: {e}. NeqSim functionality will not be available.", stacklevel=2)
elif JPYPE_AVAILABLE and jpype and jpype.isJVMStarted():
    # JVM already started, just get the package
    import jpype.imports

    neqsim = jpype.JPackage("neqsim")
