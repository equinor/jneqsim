
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jneqsim.neqsim.util.database
import jneqsim.neqsim.util.exception
import jneqsim.neqsim.util.generator
import jneqsim.neqsim.util.serialization
import jneqsim.neqsim.util.unit
import jneqsim.neqsim.util.util
import typing



class NamedInterface:
    def getName(self) -> str: ...
    def setName(self, string: str) -> None: ...

class NamedBaseClass(NamedInterface, java.io.Serializable):
    name: str = ...
    def __init__(self, string: str): ...
    def getName(self) -> str: ...
    def setName(self, string: str) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.util")``.

    NamedBaseClass: typing.Type[NamedBaseClass]
    NamedInterface: typing.Type[NamedInterface]
    database: jneqsim.neqsim.util.database.__module_protocol__
    exception: jneqsim.neqsim.util.exception.__module_protocol__
    generator: jneqsim.neqsim.util.generator.__module_protocol__
    serialization: jneqsim.neqsim.util.serialization.__module_protocol__
    unit: jneqsim.neqsim.util.unit.__module_protocol__
    util: jneqsim.neqsim.util.util.__module_protocol__
