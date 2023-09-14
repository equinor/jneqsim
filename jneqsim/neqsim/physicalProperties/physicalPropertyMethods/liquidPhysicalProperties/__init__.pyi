
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.conductivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.density
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.viscosity
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class LiquidPhysicalPropertyMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethod):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def setPhase(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties")``.

    LiquidPhysicalPropertyMethod: typing.Type[LiquidPhysicalPropertyMethod]
    conductivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.conductivity.__module_protocol__
    density: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.density.__module_protocol__
    diffusivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.diffusivity.__module_protocol__
    viscosity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.viscosity.__module_protocol__
