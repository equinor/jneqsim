
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.statistics.parameterFitting
import typing



class MonteCarloSimulation:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, statisticsBaseClass: jneqsim.neqsim.statistics.parameterFitting.StatisticsBaseClass, int: int): ...
    @typing.overload
    def __init__(self, statisticsInterface: jneqsim.neqsim.statistics.parameterFitting.StatisticsInterface): ...
    def createReportMatrix(self) -> None: ...
    def runSimulation(self) -> None: ...
    def setNumberOfRuns(self, int: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.monteCarloSimulation")``.

    MonteCarloSimulation: typing.Type[MonteCarloSimulation]
