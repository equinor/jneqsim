
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.conductivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.density
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.diffusivity
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.viscosity
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class GasPhysicalPropertyMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethod):
    binaryMolecularDiameter: typing.MutableSequence[typing.MutableSequence[float]] = ...
    binaryEnergyParameter: typing.MutableSequence[typing.MutableSequence[float]] = ...
    binaryMolecularMass: typing.MutableSequence[typing.MutableSequence[float]] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def setPhase(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties")``.

    GasPhysicalPropertyMethod: typing.Type[GasPhysicalPropertyMethod]
    conductivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.conductivity.__module_protocol__
    density: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.density.__module_protocol__
    diffusivity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.diffusivity.__module_protocol__
    viscosity: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.viscosity.__module_protocol__
