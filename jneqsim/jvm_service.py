import logging
from pathlib import Path

import jpype

neqsim_jar = Path(__file__).parent / "neqsim.jar"

if not jpype.isJVMStarted():
    if not neqsim_jar.is_file():
        raise ValueError("Missing required neqsim.jar file. Bad build?")

    jpype.startJVM(classpath=[str(neqsim_jar)], convertStrings=True)
    logging.info("JVM started")

    jvm_version = jpype.getJVMVersion()[0]
    if jvm_version < 11:
        raise OSError("Outdated Java version, Java 11 or higher is required")

import jpype.imports  # noqa

# This is the java package, added to the python scope by "jpype.imports"
import neqsim  # noqa (ruff wants to remove this line, since it's not used)


logging.debug("NeqSim successfully imported")
