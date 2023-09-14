
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.twoPhaseFlowVisualization.twoPhasePipeFlowVisualization
import typing



class TwoPhaseFlowVisualization(jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.FlowSystemVisualization):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.twoPhaseFlowVisualization")``.

    TwoPhaseFlowVisualization: typing.Type[TwoPhaseFlowVisualization]
    twoPhasePipeFlowVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.twoPhaseFlowVisualization.twoPhasePipeFlowVisualization.__module_protocol__
