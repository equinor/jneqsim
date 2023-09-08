
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jneqsim.neqsim.processSimulation.processEquipment
import jneqsim.neqsim.processSimulation.processEquipment.stream
import typing



class Filter(jneqsim.neqsim.processSimulation.processEquipment.TwoPortEquipment):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def getCvFactor(self) -> float: ...
    def getDeltaP(self) -> float: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    def runConditionAnalysis(self, processEquipmentInterface: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface) -> None: ...
    def setCvFactor(self, double: float) -> None: ...
    @typing.overload
    def setDeltaP(self, double: float) -> None: ...
    @typing.overload
    def setDeltaP(self, double: float, string: str) -> None: ...

class CharCoalFilter(Filter):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.processEquipment.filter")``.

    CharCoalFilter: typing.Type[CharCoalFilter]
    Filter: typing.Type[Filter]
