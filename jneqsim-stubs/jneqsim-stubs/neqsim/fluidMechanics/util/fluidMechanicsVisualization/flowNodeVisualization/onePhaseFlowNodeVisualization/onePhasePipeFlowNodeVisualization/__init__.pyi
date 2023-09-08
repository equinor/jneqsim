
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization
import typing



class OnePhasePipeFlowNodeVisualization(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization.OnePhaseFlowNodeVisualization):
    def __init__(self): ...
    def setData(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization.onePhasePipeFlowNodeVisualization")``.

    OnePhasePipeFlowNodeVisualization: typing.Type[OnePhasePipeFlowNodeVisualization]
