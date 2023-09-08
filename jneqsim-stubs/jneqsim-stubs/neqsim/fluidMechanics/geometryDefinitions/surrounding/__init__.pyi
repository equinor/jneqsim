
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class SurroundingEnvironment:
    def getHeatTransferCoefficient(self) -> float: ...
    def getTemperature(self) -> float: ...
    def setHeatTransferCoefficient(self, double: float) -> None: ...
    def setTemperature(self, double: float) -> None: ...

class SurroundingEnvironmentBaseClass(SurroundingEnvironment):
    def __init__(self): ...
    def getHeatTransferCoefficient(self) -> float: ...
    def getTemperature(self) -> float: ...
    def setHeatTransferCoefficient(self, double: float) -> None: ...
    def setTemperature(self, double: float) -> None: ...

class PipeSurroundingEnvironment(SurroundingEnvironmentBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.geometryDefinitions.surrounding")``.

    PipeSurroundingEnvironment: typing.Type[PipeSurroundingEnvironment]
    SurroundingEnvironment: typing.Type[SurroundingEnvironment]
    SurroundingEnvironmentBaseClass: typing.Type[SurroundingEnvironmentBaseClass]
