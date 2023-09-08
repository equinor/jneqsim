
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import neqsim
import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import typing



class ChungConductivityMethod(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.conductivity.Conductivity):
    pureComponentConductivity: typing.MutableSequence[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, physicalPropertiesInterface: jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalPropertiesInterface): ...
    def calcConductivity(self) -> float: ...
    def calcPureComponentConductivity(self) -> None: ...

class Conductivity: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.gasPhysicalProperties.conductivity")``.

    ChungConductivityMethod: typing.Type[ChungConductivityMethod]
    Conductivity: typing.Type[Conductivity]
