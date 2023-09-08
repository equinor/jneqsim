
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization.onePhasePipeFlowNodeVisualization
import typing



class OnePhaseFlowNodeVisualization(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.FlowNodeVisualization):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization")``.

    OnePhaseFlowNodeVisualization: typing.Type[OnePhaseFlowNodeVisualization]
    onePhasePipeFlowNodeVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.onePhaseFlowNodeVisualization.onePhasePipeFlowNodeVisualization.__module_protocol__
