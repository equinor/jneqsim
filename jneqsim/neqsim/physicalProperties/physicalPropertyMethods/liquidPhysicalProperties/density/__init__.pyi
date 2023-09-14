
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class Costald(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.LiquidPhysicalPropertyMethod, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface.DensityInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcDensity(self) -> float: ...
    def clone(self) -> 'Costald': ...

class Density(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.LiquidPhysicalPropertyMethod, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface.DensityInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcDensity(self) -> float: ...
    def clone(self) -> 'Density': ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.density")``.

    Costald: typing.Type[Costald]
    Density: typing.Type[Density]
