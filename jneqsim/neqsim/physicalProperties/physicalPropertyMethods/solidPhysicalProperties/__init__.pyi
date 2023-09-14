
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.conductivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.density
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.diffusivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.viscosity
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class SolidPhysicalPropertyMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethod):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def setPhase(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties")``.

    SolidPhysicalPropertyMethod: typing.Type[SolidPhysicalPropertyMethod]
    conductivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.conductivity.__module_protocol__
    density: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.density.__module_protocol__
    diffusivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.diffusivity.__module_protocol__
    viscosity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.viscosity.__module_protocol__
