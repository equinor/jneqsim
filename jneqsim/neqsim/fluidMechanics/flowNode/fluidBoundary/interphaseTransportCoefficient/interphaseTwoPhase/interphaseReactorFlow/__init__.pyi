
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseTwoPhase
import jneqsim.neqsim.thermo
import typing



class InterphaseReactorFlow(jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseTwoPhase.InterphaseTwoPhase):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface): ...

class InterphasePackedBed(InterphaseReactorFlow, jneqsim.neqsim.thermo.ThermodynamicConstantsInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface): ...
    def calcInterPhaseFrictionFactor(self, int: int, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    def calcInterphaseHeatTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    def calcInterphaseMassTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallFrictionFactor(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallFrictionFactor(self, int: int, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallHeatTransferCoefficient(self, int: int, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    @typing.overload
    def calcWallHeatTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...
    def calcWallMassTransferCoefficient(self, int: int, double: float, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseTwoPhase.interphaseReactorFlow")``.

    InterphasePackedBed: typing.Type[InterphasePackedBed]
    InterphaseReactorFlow: typing.Type[InterphaseReactorFlow]
