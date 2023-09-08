
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.standards
import jneqsim.neqsim.thermo.system
import typing



class Standard_ASTM_D6377(jneqsim.neqsim.standards.Standard):
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...
    def calculate(self) -> None: ...
    def getUnit(self, string: str) -> str: ...
    @typing.overload
    def getValue(self, string: str) -> float: ...
    @typing.overload
    def getValue(self, string: str, string2: str) -> float: ...
    def isOnSpec(self) -> bool: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.standards.oilQuality")``.

    Standard_ASTM_D6377: typing.Type[Standard_ASTM_D6377]
