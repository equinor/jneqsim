
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import jneqsim.neqsim.thermo.system
import typing



class EclipseFluidReadWrite:
    pseudoName: typing.ClassVar[str] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def read(string: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    @staticmethod
    def read(string: str, string2: str) -> jneqsim.neqsim.thermo.system.SystemInterface: ...
    @typing.overload
    @staticmethod
    def setComposition(systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def setComposition(systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, string: str, string2: str) -> None: ...

class TablePrinter(java.io.Serializable):
    def __init__(self): ...
    @staticmethod
    def printTable(stringArray: typing.Union[typing.List[typing.MutableSequence[str]], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermo.util.readwrite")``.

    EclipseFluidReadWrite: typing.Type[EclipseFluidReadWrite]
    TablePrinter: typing.Type[TablePrinter]
