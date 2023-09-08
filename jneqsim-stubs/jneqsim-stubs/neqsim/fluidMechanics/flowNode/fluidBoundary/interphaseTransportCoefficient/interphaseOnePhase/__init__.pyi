
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase.interphasePipeFlow
import typing



class InterphaseOnePhase(jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.InterphaseTransportCoefficientBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase")``.

    InterphaseOnePhase: typing.Type[InterphaseOnePhase]
    interphasePipeFlow: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.interphaseOnePhase.interphasePipeFlow.__module_protocol__
