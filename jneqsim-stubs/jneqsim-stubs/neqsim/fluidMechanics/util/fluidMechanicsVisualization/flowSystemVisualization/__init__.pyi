
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSystem
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.onePhaseFlowVisualization
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.twoPhaseFlowVisualization
import typing



class FlowSystemVisualizationInterface:
    def displayResult(self, string: str) -> None: ...
    @typing.overload
    def setNextData(self, flowSystemInterface: jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystemInterface) -> None: ...
    @typing.overload
    def setNextData(self, flowSystemInterface: jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystemInterface, double: float) -> None: ...
    def setPoints(self) -> None: ...

class FlowSystemVisualization(FlowSystemVisualizationInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    def displayResult(self, string: str) -> None: ...
    @typing.overload
    def setNextData(self, flowSystemInterface: jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystemInterface) -> None: ...
    @typing.overload
    def setNextData(self, flowSystemInterface: jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystemInterface, double: float) -> None: ...
    def setPoints(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization")``.

    FlowSystemVisualization: typing.Type[FlowSystemVisualization]
    FlowSystemVisualizationInterface: typing.Type[FlowSystemVisualizationInterface]
    onePhaseFlowVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.onePhaseFlowVisualization.__module_protocol__
    twoPhaseFlowVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.twoPhaseFlowVisualization.__module_protocol__
