
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import neqsim
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class AmineDiffusivity(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity.SiddiqiLucasMethod):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcBinaryDiffusionCoefficient(self, int: int, int2: int, int3: int) -> float: ...
    def calcDiffusionCoefficients(self, int: int, int2: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def calcEffectiveDiffusionCoefficients(self) -> None: ...

class CO2water(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity.Diffusivity):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcBinaryDiffusionCoefficient(self, int: int, int2: int, int3: int) -> float: ...

class SiddiqiLucasMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity.Diffusivity):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcBinaryDiffusionCoefficient(self, int: int, int2: int, int3: int) -> float: ...
    def calcBinaryDiffusionCoefficient2(self, int: int, int2: int, int3: int) -> float: ...

class Diffusivity: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity")``.

    AmineDiffusivity: typing.Type[AmineDiffusivity]
    CO2water: typing.Type[CO2water]
    Diffusivity: typing.Type[Diffusivity]
    SiddiqiLucasMethod: typing.Type[SiddiqiLucasMethod]