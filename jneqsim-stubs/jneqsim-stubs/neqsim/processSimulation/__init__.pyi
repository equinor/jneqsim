
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jneqsim.neqsim.processSimulation.conditionMonitor
import jneqsim.neqsim.processSimulation.controllerDevice
import jneqsim.neqsim.processSimulation.costEstimation
import jneqsim.neqsim.processSimulation.measurementDevice
import jneqsim.neqsim.processSimulation.mechanicalDesign
import jneqsim.neqsim.processSimulation.processEquipment
import jneqsim.neqsim.processSimulation.processSystem
import jneqsim.neqsim.processSimulation.util
import jneqsim.neqsim.util
import typing



class SimulationInterface(jneqsim.neqsim.util.NamedInterface, java.lang.Runnable, java.io.Serializable):
    def getCalculateSteadyState(self) -> bool: ...
    def getCalculationIdentifier(self) -> java.util.UUID: ...
    def getTime(self) -> float: ...
    def increaseTime(self, double: float) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def runTransient(self, double: float) -> None: ...
    @typing.overload
    def runTransient(self, double: float, uUID: java.util.UUID) -> None: ...
    def setCalculateSteadyState(self, boolean: bool) -> None: ...
    def setCalculationIdentifier(self, uUID: java.util.UUID) -> None: ...
    def setTime(self, double: float) -> None: ...
    def solved(self) -> bool: ...

class SimulationBaseClass(jneqsim.neqsim.util.NamedBaseClass, SimulationInterface):
    def __init__(self, string: str): ...
    def getCalculateSteadyState(self) -> bool: ...
    def getCalculationIdentifier(self) -> java.util.UUID: ...
    def getTime(self) -> float: ...
    def increaseTime(self, double: float) -> None: ...
    def setCalculateSteadyState(self, boolean: bool) -> None: ...
    def setCalculationIdentifier(self, uUID: java.util.UUID) -> None: ...
    def setTime(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation")``.

    SimulationBaseClass: typing.Type[SimulationBaseClass]
    SimulationInterface: typing.Type[SimulationInterface]
    conditionMonitor: jneqsim.neqsim.processSimulation.conditionMonitor.__module_protocol__
    controllerDevice: jneqsim.neqsim.processSimulation.controllerDevice.__module_protocol__
    costEstimation: jneqsim.neqsim.processSimulation.costEstimation.__module_protocol__
    measurementDevice: jneqsim.neqsim.processSimulation.measurementDevice.__module_protocol__
    mechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.__module_protocol__
    processEquipment: jneqsim.neqsim.processSimulation.processEquipment.__module_protocol__
    processSystem: jneqsim.neqsim.processSimulation.processSystem.__module_protocol__
    util: jneqsim.neqsim.processSimulation.util.__module_protocol__
