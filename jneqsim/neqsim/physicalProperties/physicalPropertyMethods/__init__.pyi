
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.commonPhasePhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class PhysicalPropertyMethodInterface(java.lang.Cloneable, java.io.Serializable):
    def clone(self) -> 'PhysicalPropertyMethodInterface': ...
    def setPhase(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface) -> None: ...
    def tuneModel(self, double: float, double2: float, double3: float) -> None: ...

class PhysicalPropertyMethod(PhysicalPropertyMethodInterface):
    def __init__(self): ...
    def clone(self) -> 'PhysicalPropertyMethod': ...
    def setPhase(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface) -> None: ...
    def tuneModel(self, double: float, double2: float, double3: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods")``.

    PhysicalPropertyMethod: typing.Type[PhysicalPropertyMethod]
    PhysicalPropertyMethodInterface: typing.Type[PhysicalPropertyMethodInterface]
    commonPhasePhysicalProperties: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.commonPhasePhysicalProperties.__module_protocol__
    gasPhysicalProperties: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.__module_protocol__
    liquidPhysicalProperties: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.liquidPhysicalProperties.__module_protocol__
    methodInterface: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface.__module_protocol__
    solidPhysicalProperties: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.solidPhysicalProperties.__module_protocol__
