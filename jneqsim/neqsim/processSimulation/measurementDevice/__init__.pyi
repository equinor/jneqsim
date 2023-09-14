
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jneqsim.neqsim.processSimulation.measurementDevice.online
import jneqsim.neqsim.processSimulation.measurementDevice.simpleFlowRegime
import jneqsim.neqsim.processSimulation.processEquipment.separator
import jneqsim.neqsim.processSimulation.processEquipment.stream
import jneqsim.neqsim.util
import typing



class MeasurementDeviceInterface(jneqsim.neqsim.util.NamedInterface, java.io.Serializable):
    def displayResult(self) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMaximumValue(self) -> float: ...
    def getMeasuredPercentValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    def getMinimumValue(self) -> float: ...
    def getOnlineSignal(self) -> jneqsim.neqsim.processSimulation.measurementDevice.online.OnlineSignal: ...
    def getOnlineValue(self) -> float: ...
    def getUnit(self) -> str: ...
    def hashCode(self) -> int: ...
    def isLogging(self) -> bool: ...
    def isOnlineSignal(self) -> bool: ...
    def setLogging(self, boolean: bool) -> None: ...
    def setMaximumValue(self, double: float) -> None: ...
    def setMinimumValue(self, double: float) -> None: ...
    def setUnit(self, string: str) -> None: ...

class MeasurementDeviceBaseClass(jneqsim.neqsim.util.NamedBaseClass, MeasurementDeviceInterface):
    def __init__(self, string: str, string2: str): ...
    def displayResult(self) -> None: ...
    def doConditionAnalysis(self) -> bool: ...
    def getConditionAnalysisMaxDeviation(self) -> float: ...
    def getConditionAnalysisMessage(self) -> str: ...
    def getMaximumValue(self) -> float: ...
    def getMeasuredPercentValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def getMinimumValue(self) -> float: ...
    def getOnlineMeasurementValue(self) -> float: ...
    def getOnlineSignal(self) -> jneqsim.neqsim.processSimulation.measurementDevice.online.OnlineSignal: ...
    def getUnit(self) -> str: ...
    def isLogging(self) -> bool: ...
    def isOnlineSignal(self) -> bool: ...
    def runConditionAnalysis(self) -> None: ...
    def setConditionAnalysis(self, boolean: bool) -> None: ...
    def setConditionAnalysisMaxDeviation(self, double: float) -> None: ...
    def setIsOnlineSignal(self, boolean: bool, string: str, string2: str) -> None: ...
    def setLogging(self, boolean: bool) -> None: ...
    def setMaximumValue(self, double: float) -> None: ...
    def setMinimumValue(self, double: float) -> None: ...
    def setOnlineMeasurementValue(self, double: float, string: str) -> None: ...
    def setOnlineSignal(self, onlineSignal: jneqsim.neqsim.processSimulation.measurementDevice.online.OnlineSignal) -> None: ...
    def setQualityCheckMessage(self, string: str) -> None: ...
    def setUnit(self, string: str) -> None: ...

class LevelTransmitter(MeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, separator: jneqsim.neqsim.processSimulation.processEquipment.separator.Separator): ...
    @typing.overload
    def __init__(self, separator: jneqsim.neqsim.processSimulation.processEquipment.separator.Separator): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...

class StreamMeasurementDeviceBaseClass(MeasurementDeviceBaseClass):
    def __init__(self, string: str, string2: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def getStream(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def setStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...

class CombustionEmissionsCalculator(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @staticmethod
    def calculateCO2Emissions(map: typing.Union[java.util.Map[str, float], typing.Mapping[str, float]], map2: typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]) -> float: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def setComponents(self) -> None: ...

class CricondenbarAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def getMeasuredValue2(self, string: str, double: float) -> float: ...

class HydrateEquilibriumTemperatureAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def getReferencePressure(self) -> float: ...
    def setReferencePressure(self, double: float) -> None: ...

class MolarMassAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...

class MultiPhaseMeter(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str, string2: str) -> float: ...
    def getPressure(self) -> float: ...
    def getTemperature(self) -> float: ...
    def setPressure(self, double: float, string: str) -> None: ...
    def setTemperature(self, double: float, string: str) -> None: ...

class NMVOCAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def getnmVOCFlowRate(self, string: str) -> float: ...

class PressureTransmitter(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...

class TemperatureTransmitter(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...

class VolumeFlowTransmitter(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    def getMeasuredPhaseNumber(self) -> int: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def setMeasuredPhaseNumber(self, int: int) -> None: ...

class WaterContentAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...

class WaterDewPointAnalyser(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def displayResult(self) -> None: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def getMethod(self) -> str: ...
    def getReferencePressure(self) -> float: ...
    def setMethod(self, string: str) -> None: ...
    def setReferencePressure(self, double: float) -> None: ...

class WellAllocator(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str, string2: str) -> float: ...
    def setExportGasStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...
    def setExportOilStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...

class pHProbe(StreamMeasurementDeviceBaseClass):
    @typing.overload
    def __init__(self, string: str, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    @typing.overload
    def __init__(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface): ...
    def getAlkalinity(self) -> float: ...
    def getAlkanility(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self) -> float: ...
    @typing.overload
    def getMeasuredValue(self, string: str) -> float: ...
    def run(self) -> None: ...
    def setAlkalinity(self, double: float) -> None: ...
    def setAlkanility(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.measurementDevice")``.

    CombustionEmissionsCalculator: typing.Type[CombustionEmissionsCalculator]
    CricondenbarAnalyser: typing.Type[CricondenbarAnalyser]
    HydrateEquilibriumTemperatureAnalyser: typing.Type[HydrateEquilibriumTemperatureAnalyser]
    LevelTransmitter: typing.Type[LevelTransmitter]
    MeasurementDeviceBaseClass: typing.Type[MeasurementDeviceBaseClass]
    MeasurementDeviceInterface: typing.Type[MeasurementDeviceInterface]
    MolarMassAnalyser: typing.Type[MolarMassAnalyser]
    MultiPhaseMeter: typing.Type[MultiPhaseMeter]
    NMVOCAnalyser: typing.Type[NMVOCAnalyser]
    PressureTransmitter: typing.Type[PressureTransmitter]
    StreamMeasurementDeviceBaseClass: typing.Type[StreamMeasurementDeviceBaseClass]
    TemperatureTransmitter: typing.Type[TemperatureTransmitter]
    VolumeFlowTransmitter: typing.Type[VolumeFlowTransmitter]
    WaterContentAnalyser: typing.Type[WaterContentAnalyser]
    WaterDewPointAnalyser: typing.Type[WaterDewPointAnalyser]
    WellAllocator: typing.Type[WellAllocator]
    pHProbe: typing.Type[pHProbe]
    online: jneqsim.neqsim.processSimulation.measurementDevice.online.__module_protocol__
    simpleFlowRegime: jneqsim.neqsim.processSimulation.measurementDevice.simpleFlowRegime.__module_protocol__