
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter.twoPhasePipeFlowFileWriter
import typing



class TwoPhaseFileWriter(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.FileWriterBaseClass):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter")``.

    TwoPhaseFileWriter: typing.Type[TwoPhaseFileWriter]
    twoPhasePipeFlowFileWriter: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.twoPhaseFileWriter.twoPhasePipeFlowFileWriter.__module_protocol__
