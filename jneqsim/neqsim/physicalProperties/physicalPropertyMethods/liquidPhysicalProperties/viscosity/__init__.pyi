
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class Viscosity(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.LiquidPhysicalPropertyMethod, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface.ViscosityInterface):
    pureComponentViscosity: typing.MutableSequence[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcPureComponentViscosity(self) -> None: ...
    def calcViscosity(self) -> float: ...
    def clone(self) -> 'Viscosity': ...
    def getPureComponentViscosity(self, int: int) -> float: ...
    def getViscosityPressureCorrection(self, int: int) -> float: ...

class AmineViscosity(Viscosity):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcViscosity(self) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.viscosity")``.

    AmineViscosity: typing.Type[AmineViscosity]
    Viscosity: typing.Type[Viscosity]
