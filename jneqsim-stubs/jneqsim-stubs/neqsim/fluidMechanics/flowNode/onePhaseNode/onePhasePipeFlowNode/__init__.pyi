
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.fluidMechanics.flowNode.onePhaseNode
import jneqsim.neqsim.fluidMechanics.geometryDefinitions
import jneqsim.neqsim.thermo.system
import typing



class onePhasePipeFlowNode(jneqsim.neqsim.fluidMechanics.flowNode.onePhaseNode.onePhaseFlowNode):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, geometryDefinitionInterface: jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinitionInterface): ...
    def calcReynoldsNumber(self) -> float: ...
    def clone(self) -> 'onePhasePipeFlowNode': ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.onePhaseNode.onePhasePipeFlowNode")``.

    onePhasePipeFlowNode: typing.Type[onePhasePipeFlowNode]
