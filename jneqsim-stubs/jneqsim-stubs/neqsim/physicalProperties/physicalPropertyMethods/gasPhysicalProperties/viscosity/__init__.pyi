
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import neqsim
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class ChungViscosityMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.viscosity.Viscosity):
    pureComponentViscosity: typing.MutableSequence[float] = ...
    relativeViscosity: typing.MutableSequence[float] = ...
    Fc: typing.MutableSequence[float] = ...
    omegaVisc: typing.MutableSequence[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcViscosity(self) -> float: ...
    def getPureComponentViscosity(self, int: int) -> float: ...
    def initChungPureComponentViscosity(self) -> None: ...

class Viscosity: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.viscosity")``.

    ChungViscosityMethod: typing.Type[ChungViscosityMethod]
    Viscosity: typing.Type[Viscosity]
