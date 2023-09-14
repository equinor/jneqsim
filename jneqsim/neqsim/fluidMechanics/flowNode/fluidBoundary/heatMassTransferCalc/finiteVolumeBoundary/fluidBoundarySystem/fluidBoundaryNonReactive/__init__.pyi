
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem
import typing



class FluidBoundarySystemNonReactive(jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem.FluidBoundarySystem):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, fluidBoundaryInterface: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.FluidBoundaryInterface): ...
    def createSystem(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem.fluidBoundaryNonReactive")``.

    FluidBoundarySystemNonReactive: typing.Type[FluidBoundarySystemNonReactive]
