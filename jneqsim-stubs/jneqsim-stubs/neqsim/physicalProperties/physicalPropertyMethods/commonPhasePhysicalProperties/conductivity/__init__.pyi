
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import neqsim
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import jneqsim.neqsim.thermo.system
import typing



class PFCTConductivityMethodMod86(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.commonPhasePhysicalProperties.conductivity.Conductivity):
    referenceSystem: typing.ClassVar[jneqsim.neqsim.thermo.system.SystemInterface] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcConductivity(self) -> float: ...
    def calcMixLPViscosity(self) -> float: ...
    def getRefComponentConductivity(self, double: float, double2: float) -> float: ...
    def getRefComponentViscosity(self, double: float, double2: float) -> float: ...

class Conductivity: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.commonPhasePhysicalProperties.conductivity")``.

    Conductivity: typing.Type[Conductivity]
    PFCTConductivityMethodMod86: typing.Type[PFCTConductivityMethodMod86]
