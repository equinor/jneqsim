
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.multiPhaseNode
import jneqsim.neqsim.fluidMechanics.flowNode.twoPhaseNode.twoPhasePipeFlowNode
import jneqsim.neqsim.fluidMechanics.geometryDefinitions
import jneqsim.neqsim.thermo.system
import typing



class WaxDepositionFlowNode(jneqsim.neqsim.fluidMechanics.flowNode.multiPhaseNode.MultiPhaseFlowNode):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, geometryDefinitionInterface: jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinitionInterface): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, systemInterface2: jneqsim.neqsim.thermo.system.SystemInterface, geometryDefinitionInterface: jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinitionInterface): ...
    def calcContactLength(self) -> float: ...
    def clone(self) -> jneqsim.neqsim.fluidMechanics.flowNode.twoPhaseNode.twoPhasePipeFlowNode.StratifiedFlowNode: ...
    def getNextNode(self) -> jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface: ...
    def init(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.multiPhaseNode.waxNode")``.

    WaxDepositionFlowNode: typing.Type[WaxDepositionFlowNode]
