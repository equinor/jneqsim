
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.thermo.system
import jneqsim.neqsim.thermodynamicOperations
import org.jfree.chart
import typing



class ChemicalEquilibrium(jneqsim.neqsim.thermodynamicOperations.BaseOperation):
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...
    def displayResult(self) -> None: ...
    def getJFreeChart(self, string: str) -> org.jfree.chart.JFreeChart: ...
    def getPoints(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getResultTable(self) -> typing.MutableSequence[typing.MutableSequence[str]]: ...
    def printToFile(self, string: str) -> None: ...
    def run(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermodynamicOperations.chemicalEquilibrium")``.

    ChemicalEquilibrium: typing.Type[ChemicalEquilibrium]
