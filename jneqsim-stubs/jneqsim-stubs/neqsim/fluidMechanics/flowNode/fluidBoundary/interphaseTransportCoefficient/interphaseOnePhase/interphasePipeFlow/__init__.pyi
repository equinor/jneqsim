
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase
import typing



class InterphasePipeFlow(jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase.InterphaseOnePhase):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface): ...
    @typing.overload
    def calcWallFrictionFactor(self, int: int, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallFrictionFactor(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallHeatTransferCoefficient(self, int: int, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallHeatTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    def calcWallMassTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase.interphasePipeFlow")``.

    InterphasePipeFlow: typing.Type[InterphasePipeFlow]
