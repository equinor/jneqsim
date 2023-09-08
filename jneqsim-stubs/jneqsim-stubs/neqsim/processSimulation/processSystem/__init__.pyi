
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import jneqsim.neqsim.processSimulation
import jneqsim.neqsim.processSimulation.conditionMonitor
import jneqsim.neqsim.processSimulation.controllerDevice
import jneqsim.neqsim.processSimulation.measurementDevice
import jneqsim.neqsim.processSimulation.mechanicalDesign
import jneqsim.neqsim.processSimulation.processEquipment
import jneqsim.neqsim.processSimulation.processEquipment.stream
import jneqsim.neqsim.processSimulation.processSystem.processModules
import jneqsim.neqsim.thermo.system
import typing



class ModuleInterface(jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface):
    def addInputStream(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getOperations(self) -> 'ProcessSystem': ...
    def getOutputStream(self, string: str) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getPreferedThermodynamicModel(self) -> str: ...
    def getUnit(self, string: str) -> typing.Any: ...
    def hashCode(self) -> int: ...
    def initializeModule(self) -> None: ...
    def initializeStreams(self) -> None: ...
    def isCalcDesign(self) -> bool: ...
    def setIsCalcDesign(self, boolean: bool) -> None: ...
    def setPreferedThermodynamicModel(self, string: str) -> None: ...
    def setProperty(self, string: str, double: float) -> None: ...

class ProcessModule(jneqsim.neqsim.processSimulation.SimulationBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def add(self, processModule: 'ProcessModule') -> None: ...
    @typing.overload
    def add(self, processSystem: 'ProcessSystem') -> None: ...
    def checkModulesRecycles(self) -> None: ...
    def copy(self) -> 'ProcessModule': ...
    def getAddedModules(self) -> java.util.List['ProcessModule']: ...
    def getAddedUnitOperations(self) -> java.util.List['ProcessSystem']: ...
    def getModulesIndex(self) -> java.util.List[int]: ...
    def getOperationsIndex(self) -> java.util.List[int]: ...
    def getUnit(self, string: str) -> typing.Any: ...
    def recyclesSolved(self) -> bool: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    def runAsThread(self) -> java.lang.Thread: ...
    def solved(self) -> bool: ...

class ProcessSystem(jneqsim.neqsim.processSimulation.SimulationBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def add(self, measurementDeviceInterface: jneqsim.neqsim.processSimulation.measurementDevice.MeasurementDeviceInterface) -> None: ...
    @typing.overload
    def add(self, processEquipmentInterface: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface) -> None: ...
    @typing.overload
    def add(self, processEquipmentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface], jpype.JArray]) -> None: ...
    def clear(self) -> None: ...
    def clearAll(self) -> None: ...
    def copy(self) -> 'ProcessSystem': ...
    def displayResult(self) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAllUnitNames(self) -> java.util.ArrayList[str]: ...
    def getConditionMonitor(self) -> jneqsim.neqsim.processSimulation.conditionMonitor.ConditionMonitor: ...
    def getCoolerDuty(self, string: str) -> float: ...
    def getEntropyProduction(self, string: str) -> float: ...
    def getExergyChange(self, string: str) -> float: ...
    def getHeaterDuty(self, string: str) -> float: ...
    def getMeasurementDevice(self, string: str) -> typing.Any: ...
    def getName(self) -> str: ...
    def getPower(self, string: str) -> float: ...
    def getSurroundingTemperature(self) -> float: ...
    @typing.overload
    def getTime(self) -> float: ...
    @typing.overload
    def getTime(self, string: str) -> float: ...
    def getTimeStep(self) -> float: ...
    def getUnit(self, string: str) -> typing.Any: ...
    def getUnitNumber(self, string: str) -> int: ...
    def getUnitOperations(self) -> java.util.ArrayList[jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface]: ...
    def hasUnitName(self, string: str) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def open(string: str) -> 'ProcessSystem': ...
    def printLogFile(self, string: str) -> None: ...
    def removeUnit(self, string: str) -> None: ...
    def replaceObject(self, string: str, processEquipmentBaseClass: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentBaseClass) -> None: ...
    def reportMeasuredValues(self) -> None: ...
    def reportResults(self) -> typing.MutableSequence[typing.MutableSequence[str]]: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    def runAsThread(self) -> java.lang.Thread: ...
    @typing.overload
    def runTransient(self, double: float) -> None: ...
    @typing.overload
    def runTransient(self) -> None: ...
    @typing.overload
    def runTransient(self, double: float, uUID: java.util.UUID) -> None: ...
    def save(self, string: str) -> None: ...
    @typing.overload
    def setFluid(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, systemInterface2: jneqsim.neqsim.thermo.system.SystemInterface) -> None: ...
    @typing.overload
    def setFluid(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, systemInterface2: jneqsim.neqsim.thermo.system.SystemInterface, boolean: bool) -> None: ...
    def setName(self, string: str) -> None: ...
    def setSurroundingTemperature(self, double: float) -> None: ...
    def setTimeStep(self, double: float) -> None: ...
    def size(self) -> int: ...
    def solved(self) -> bool: ...
    def view(self) -> None: ...

class ProcessModuleBaseClass(jneqsim.neqsim.processSimulation.SimulationBaseClass, ModuleInterface):
    def __init__(self, string: str): ...
    def calcDesign(self) -> None: ...
    def displayResult(self) -> None: ...
    def getConditionAnalysisMessage(self) -> str: ...
    def getController(self) -> jneqsim.neqsim.processSimulation.controllerDevice.ControllerDeviceInterface: ...
    def getEntropyProduction(self, string: str) -> float: ...
    def getExergyChange(self, string: str, double: float) -> float: ...
    def getMassBalance(self, string: str) -> float: ...
    def getMechanicalDesign(self) -> jneqsim.neqsim.processSimulation.mechanicalDesign.MechanicalDesign: ...
    def getOperations(self) -> ProcessSystem: ...
    def getPreferedThermodynamicModel(self) -> str: ...
    @typing.overload
    def getPressure(self) -> float: ...
    @typing.overload
    def getPressure(self, string: str) -> float: ...
    def getResultTable(self) -> typing.MutableSequence[typing.MutableSequence[str]]: ...
    def getSpecification(self) -> str: ...
    def getThermoSystem(self) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    def getUnit(self, string: str) -> typing.Any: ...
    def isCalcDesign(self) -> bool: ...
    def reportResults(self) -> typing.MutableSequence[typing.MutableSequence[str]]: ...
    def runConditionAnalysis(self, processEquipmentInterface: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface) -> None: ...
    @typing.overload
    def runTransient(self, double: float) -> None: ...
    @typing.overload
    def runTransient(self, double: float, uUID: java.util.UUID) -> None: ...
    def setController(self, controllerDeviceInterface: jneqsim.neqsim.processSimulation.controllerDevice.ControllerDeviceInterface) -> None: ...
    def setDesign(self) -> None: ...
    def setIsCalcDesign(self, boolean: bool) -> None: ...
    def setPreferedThermodynamicModel(self, string: str) -> None: ...
    def setPressure(self, double: float) -> None: ...
    @typing.overload
    def setProperty(self, string: str, double: float) -> None: ...
    @typing.overload
    def setProperty(self, string: str, double: float, string2: str) -> None: ...
    def setRegulatorOutSignal(self, double: float) -> None: ...
    @typing.overload
    def setSpecification(self, string: str) -> None: ...
    @typing.overload
    def setSpecification(self, string: str, double: float) -> None: ...
    def solved(self) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.processSystem")``.

    ModuleInterface: typing.Type[ModuleInterface]
    ProcessModule: typing.Type[ProcessModule]
    ProcessModuleBaseClass: typing.Type[ProcessModuleBaseClass]
    ProcessSystem: typing.Type[ProcessSystem]
    processModules: jneqsim.neqsim.processSimulation.processSystem.processModules.__module_protocol__
