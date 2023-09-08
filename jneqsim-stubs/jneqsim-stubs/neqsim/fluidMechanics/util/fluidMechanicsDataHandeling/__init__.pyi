
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter
import typing



class FileWriterBaseClass(java.io.Serializable):
    def __init__(self): ...

class FileWriterInterface: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling")``.

    FileWriterBaseClass: typing.Type[FileWriterBaseClass]
    FileWriterInterface: typing.Type[FileWriterInterface]
    onePhaseFileWriter: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter.__module_protocol__
    twoPhaseFileWriter: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter.__module_protocol__
