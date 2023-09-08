
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import typing



class methaneBWR32:
    def __init__(self): ...
    def calcPressure(self, double: float, double2: float) -> float: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def molDens(self, double: float, double2: float, boolean: bool) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermo.util.referenceEquations")``.

    methaneBWR32: typing.Type[methaneBWR32]
