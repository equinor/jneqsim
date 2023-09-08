
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.geometryDefinitions
import typing



class ReactorData(jneqsim.neqsim.fluidMechanics.geometryDefinitions.GeometryDefinition):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def clone(self) -> 'ReactorData': ...
    @typing.overload
    def setPackingType(self, int: int) -> None: ...
    @typing.overload
    def setPackingType(self, string: str) -> None: ...
    @typing.overload
    def setPackingType(self, string: str, string2: str, int: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.geometryDefinitions.reactor")``.

    ReactorData: typing.Type[ReactorData]
