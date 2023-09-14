
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem
import typing



class TwoPhasePipeFlowSystem(jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.TwoPhaseFlowSystem):
    def __init__(self): ...
    def createSystem(self) -> None: ...
    def init(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    @typing.overload
    def solveSteadyState(self, int: int) -> None: ...
    @typing.overload
    def solveSteadyState(self, int: int, uUID: java.util.UUID) -> None: ...
    @typing.overload
    def solveTransient(self, int: int) -> None: ...
    @typing.overload
    def solveTransient(self, int: int, uUID: java.util.UUID) -> None: ...

class TwoPhasePipeFlowSystemReac(TwoPhasePipeFlowSystem):
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.twoPhasePipeFlowSystem")``.

    TwoPhasePipeFlowSystem: typing.Type[TwoPhasePipeFlowSystem]
    TwoPhasePipeFlowSystemReac: typing.Type[TwoPhasePipeFlowSystemReac]
