
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jneqsim.neqsim.processSimulation.processEquipment
import jneqsim.neqsim.processSimulation.processEquipment.stream
import jneqsim.neqsim.thermo.system
import typing



class Tank(jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def addStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...
    def displayResult(self) -> None: ...
    def getEfficiency(self) -> float: ...
    def getGas(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getGasCarryunderFraction(self) -> float: ...
    def getGasOutStream(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getLiquid(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getLiquidCarryoverFraction(self) -> float: ...
    def getLiquidLevel(self) -> float: ...
    def getLiquidOutStream(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getVolume(self) -> float: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    @typing.overload
    def runTransient(self, double: float) -> None: ...
    @typing.overload
    def runTransient(self, double: float, uUID: java.util.UUID) -> None: ...
    def setEfficiency(self, double: float) -> None: ...
    def setGasCarryunderFraction(self, double: float) -> None: ...
    def setInletStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...
    def setLiquidCarryoverFraction(self, double: float) -> None: ...
    def setOutComposition(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface) -> None: ...
    def setTempPres(self, double: float, double2: float) -> None: ...
    def setVolume(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.processEquipment.tank")``.

    Tank: typing.Type[Tank]