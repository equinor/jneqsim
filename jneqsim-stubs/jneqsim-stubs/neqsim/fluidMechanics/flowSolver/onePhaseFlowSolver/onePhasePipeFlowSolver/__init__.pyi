
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver
import jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem.pipeFlowSystem
import jneqsim.neqsim.thermo
import typing



class OnePhasePipeFlowSolver(jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver.OnePhaseFlowSolver):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, pipeFlowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem.pipeFlowSystem.PipeFlowSystem, double: float, int: int): ...
    def clone(self) -> 'OnePhasePipeFlowSolver': ...

class OnePhaseFixedStaggeredGrid(OnePhasePipeFlowSolver, jneqsim.neqsim.thermo.ThermodynamicConstantsInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, pipeFlowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem.pipeFlowSystem.PipeFlowSystem, double: float, int: int, boolean: bool): ...
    def clone(self) -> 'OnePhaseFixedStaggeredGrid': ...
    def initComposition(self, int: int) -> None: ...
    def initFinalResults(self) -> None: ...
    def initMatrix(self) -> None: ...
    def initPressure(self, int: int) -> None: ...
    def initProfiles(self) -> None: ...
    def initTemperature(self, int: int) -> None: ...
    def initVelocity(self, int: int) -> None: ...
    def setComponentConservationMatrix(self, int: int) -> None: ...
    def setEnergyMatrixTDMA(self) -> None: ...
    def setImpulsMatrixTDMA(self) -> None: ...
    def setMassConservationMatrixTDMA(self) -> None: ...
    def solveTDMA(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver.onePhasePipeFlowSolver")``.

    OnePhaseFixedStaggeredGrid: typing.Type[OnePhaseFixedStaggeredGrid]
    OnePhasePipeFlowSolver: typing.Type[OnePhasePipeFlowSolver]
