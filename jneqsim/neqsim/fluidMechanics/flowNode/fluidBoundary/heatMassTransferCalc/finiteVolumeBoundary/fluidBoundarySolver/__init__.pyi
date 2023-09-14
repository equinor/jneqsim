
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySolver.fluidBoundaryReactiveSolver
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem
import typing



class FluidBoundarySolverInterface:
    def getMolarFlux(self, int: int) -> float: ...
    def solve(self) -> None: ...

class FluidBoundarySolver(FluidBoundarySolverInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, fluidBoundarySystemInterface: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem.FluidBoundarySystemInterface): ...
    @typing.overload
    def __init__(self, fluidBoundarySystemInterface: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySystem.FluidBoundarySystemInterface, boolean: bool): ...
    def getMolarFlux(self, int: int) -> float: ...
    def initComposition(self, int: int) -> None: ...
    def initMatrix(self) -> None: ...
    def initProfiles(self) -> None: ...
    def setComponentConservationMatrix(self, int: int) -> None: ...
    def solve(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySolver")``.

    FluidBoundarySolver: typing.Type[FluidBoundarySolver]
    FluidBoundarySolverInterface: typing.Type[FluidBoundarySolverInterface]
    fluidBoundaryReactiveSolver: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundarySolver.fluidBoundaryReactiveSolver.__module_protocol__
