
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter.pipeFlowFileWriter
import typing



class OnePhaseFileWriter(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.FileWriterBaseClass):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter")``.

    OnePhaseFileWriter: typing.Type[OnePhaseFileWriter]
    pipeFlowFileWriter: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter.pipeFlowFileWriter.__module_protocol__
