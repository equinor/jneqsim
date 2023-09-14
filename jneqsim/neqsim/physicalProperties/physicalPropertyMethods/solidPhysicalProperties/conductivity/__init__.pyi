
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class Conductivity(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.SolidPhysicalPropertyMethod, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface.ConductivityInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcConductivity(self) -> float: ...
    def clone(self) -> 'Conductivity': ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.conductivity")``.

    Conductivity: typing.Type[Conductivity]
