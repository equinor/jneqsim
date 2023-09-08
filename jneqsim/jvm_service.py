import logging
from pathlib import Path

import jpype

if not jpype.isJVMStarted():
    neqsim_jar_path = str(Path(__file__).parent / "neqsim.jar")
    jpype.startJVM(classpath=[neqsim_jar_path], convertStrings=True)
    logging.info("JVM started")

    jvm_version = jpype.getJVMVersion()[0]
    if jvm_version < 11:
        raise OSError("Outdated Java version, Java 11 or higher is required")
import jpype.imports
import neqsim as java_neqsim

logging.debug("NeqSim successfully imported")

neqsim = java_neqsim
