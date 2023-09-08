
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc
import jneqsim.neqsim.thermo.system
import typing



class EquilibriumFluidBoundary(jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.FluidBoundary):
    @typing.overload
    def __init__(self, flowNodeInterface: jneqsim.neqsim.fluidMechanics.flowNode.FlowNodeInterface): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...
    def calcFluxes(self) -> typing.MutableSequence[float]: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def solve(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.equilibriumFluidBoundary")``.

    EquilibriumFluidBoundary: typing.Type[EquilibriumFluidBoundary]
