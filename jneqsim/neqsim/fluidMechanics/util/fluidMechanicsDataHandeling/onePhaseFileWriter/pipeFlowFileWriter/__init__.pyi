
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter
import typing



class PipeFlowFileWriter(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter.OnePhaseFileWriter):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.onePhaseFileWriter.pipeFlowFileWriter")``.

    PipeFlowFileWriter: typing.Type[PipeFlowFileWriter]
