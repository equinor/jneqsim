
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter
import typing



class TwoPhasePipeFlowFileWriter(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter.TwoPhaseFileWriter):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter.twoPhasePipeFlowFileWriter")``.

    TwoPhasePipeFlowFileWriter: typing.Type[TwoPhasePipeFlowFileWriter]
