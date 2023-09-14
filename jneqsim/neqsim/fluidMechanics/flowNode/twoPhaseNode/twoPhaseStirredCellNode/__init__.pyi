
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.twoPhaseNode
import jneqsim.neqsim.fluidMechanics.geometryDefinitions
import jneqsim.neqsim.thermo.system
import typing



class StirredCellNode(jneqsim.neqsim.fluidMechanics.flowNode.twoPhaseNode.TwoPhaseFlowNode):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, geometryDefinitionInterface: jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinitionInterface): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, systemInterface2: jneqsim.neqsim.thermo.system.SystemInterface, geometryDefinitionInterface: jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinitionInterface): ...
    def calcContactLength(self) -> float: ...
    def calcGasLiquidContactArea(self) -> float: ...
    def calcHydraulicDiameter(self) -> float: ...
    def calcReynoldNumber(self) -> float: ...
    def clone(self) -> 'StirredCellNode': ...
    def getDt(self) -> float: ...
    def getNextNode(self) -> jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface: ...
    def getStirrerDiameter(self) -> typing.MutableSequence[float]: ...
    def getStirrerRate(self, int: int) -> float: ...
    def init(self) -> None: ...
    def initFlowCalc(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def setDt(self, double: float) -> None: ...
    @typing.overload
    def setStirrerDiameter(self, double: float) -> None: ...
    @typing.overload
    def setStirrerDiameter(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def setStirrerSpeed(self, double: float) -> None: ...
    @typing.overload
    def setStirrerSpeed(self, int: int, double: float) -> None: ...
    @typing.overload
    def update(self, double: float) -> None: ...
    @typing.overload
    def update(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.twoPhaseNode.twoPhaseStirredCellNode")``.

    StirredCellNode: typing.Type[StirredCellNode]