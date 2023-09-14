
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import jneqsim.neqsim.physicalProperties.interfaceProperties
import jneqsim.neqsim.physicalProperties.mixingRule
import jneqsim.neqsim.physicalProperties.physicalPropertyMethods
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import jneqsim.neqsim.physicalProperties.util
import jneqsim.neqsim.thermo.phase
import typing



class PhysicalPropertyHandler(java.lang.Cloneable, java.io.Serializable):
    def __init__(self): ...
    def clone(self) -> 'PhysicalPropertyHandler': ...
    def getPhysicalProperty(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface: ...
    def setPhysicalProperties(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, int: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties")``.

    PhysicalPropertyHandler: typing.Type[PhysicalPropertyHandler]
    interfaceProperties: jneqsim.neqsim.physicalProperties.interfaceProperties.__module_protocol__
    mixingRule: jneqsim.neqsim.physicalProperties.mixingRule.__module_protocol__
    physicalPropertyMethods: jneqsim.neqsim.physicalProperties.physicalPropertyMethods.__module_protocol__
    physicalPropertySystem: jneqsim.neqsim.physicalProperties.physicalPropertySystem.__module_protocol__
    util: jneqsim.neqsim.physicalProperties.util.__module_protocol__
