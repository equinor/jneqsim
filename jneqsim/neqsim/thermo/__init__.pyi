
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import jneqsim.neqsim.thermo.atomElement
import jneqsim.neqsim.thermo.characterization
import jneqsim.neqsim.thermo.component
import jneqsim.neqsim.thermo.mixingRule
import jneqsim.neqsim.thermo.phase
import jneqsim.neqsim.thermo.system
import jneqsim.neqsim.thermo.util
import typing



class Fluid:
    def __init__(self): ...
    def addComponment(self, string: str) -> None: ...
    def create(self, string: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    def create2(self, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    def create2(self, stringArray: typing.Union[typing.List[str], jpype.JArray], doubleArray: typing.Union[typing.List[float], jpype.JArray], string2: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    def createFluid(self, stringArray: typing.Union[typing.List[str], jpype.JArray], doubleArray: typing.Union[typing.List[float], jpype.JArray], string2: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    def getFluid(self) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    def getThermoMixingRule(self) -> str: ...
    def getThermoModel(self) -> str: ...
    def isAutoSelectModel(self) -> bool: ...
    def isHasWater(self) -> bool: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def setAutoSelectModel(self, boolean: bool) -> None: ...
    def setHasWater(self, boolean: bool) -> None: ...
    def setThermoMixingRule(self, string: str) -> None: ...
    def setThermoModel(self, string: str) -> None: ...

class FluidCreator:
    hasWater: typing.ClassVar[bool] = ...
    autoSelectModel: typing.ClassVar[bool] = ...
    thermoModel: typing.ClassVar[str] = ...
    thermoMixingRule: typing.ClassVar[str] = ...
    @typing.overload
    @staticmethod
    def create(string: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    @staticmethod
    def create(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    @staticmethod
    def create(stringArray: typing.Union[typing.List[str], jpype.JArray], doubleArray: typing.Union[typing.List[float], jpype.JArray], string2: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...

class ThermodynamicConstantsInterface(java.io.Serializable):
    R: typing.ClassVar[float] = ...
    pi: typing.ClassVar[float] = ...
    gravity: typing.ClassVar[float] = ...
    avagadroNumber: typing.ClassVar[float] = ...
    MAX_NUMBER_OF_COMPONENTS: typing.ClassVar[int] = ...
    referenceTemperature: typing.ClassVar[float] = ...
    referencePressure: typing.ClassVar[float] = ...
    atm: typing.ClassVar[float] = ...
    boltzmannConstant: typing.ClassVar[float] = ...
    electronCharge: typing.ClassVar[float] = ...
    planckConstant: typing.ClassVar[float] = ...
    vacumPermittivity: typing.ClassVar[float] = ...
    faradayConstant: typing.ClassVar[float] = ...
    standardStateTemperature: typing.ClassVar[float] = ...
    normalStateTemperature: typing.ClassVar[float] = ...
    molarMassAir: typing.ClassVar[float] = ...

class ThermodynamicModelSettings(java.io.Serializable):
    phaseFractionMinimumLimit: typing.ClassVar[float] = ...
    MAX_NUMBER_OF_COMPONENTS: typing.ClassVar[int] = ...

class ThermodynamicModelTest(ThermodynamicConstantsInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...
    def checkFugacityCoefficients(self) -> bool: ...
    def checkFugacityCoefficientsDP(self) -> bool: ...
    def checkFugacityCoefficientsDT(self) -> bool: ...
    def checkFugacityCoefficientsDn(self) -> bool: ...
    def checkFugacityCoefficientsDn2(self) -> bool: ...
    def checkNumerically(self) -> bool: ...
    def runTest(self) -> None: ...
    def setMaxError(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermo")``.

    Fluid: typing.Type[Fluid]
    FluidCreator: typing.Type[FluidCreator]
    ThermodynamicConstantsInterface: typing.Type[ThermodynamicConstantsInterface]
    ThermodynamicModelSettings: typing.Type[ThermodynamicModelSettings]
    ThermodynamicModelTest: typing.Type[ThermodynamicModelTest]
    atomElement: jneqsim.neqsim.thermo.atomElement.__module_protocol__
    characterization: jneqsim.neqsim.thermo.characterization.__module_protocol__
    component: jneqsim.neqsim.thermo.component.__module_protocol__
    mixingRule: jneqsim.neqsim.thermo.mixingRule.__module_protocol__
    phase: jneqsim.neqsim.thermo.phase.__module_protocol__
    system: jneqsim.neqsim.thermo.system.__module_protocol__
    util: jneqsim.neqsim.thermo.util.__module_protocol__