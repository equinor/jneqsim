
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowLeg
import jneqsim.neqsim.fluidMechanics.flowNode
import typing



class PipeLeg(jneqsim.neqsim.fluidMechanics.flowLeg.FlowLeg):
    def __init__(self): ...
    @typing.overload
    def createFlowNodes(self) -> None: ...
    @typing.overload
    def createFlowNodes(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowLeg.pipeLeg")``.

    PipeLeg: typing.Type[PipeLeg]
