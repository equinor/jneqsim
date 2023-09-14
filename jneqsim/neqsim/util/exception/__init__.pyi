
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class ThermoException(java.lang.Exception):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class InvalidInputException(ThermoException):
    @typing.overload
    def __init__(self, object: typing.Any, string: str, string2: str): ...
    @typing.overload
    def __init__(self, object: typing.Any, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...

class IsNaNException(ThermoException):
    @typing.overload
    def __init__(self, object: typing.Any, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class NotInitializedException(ThermoException):
    @typing.overload
    def __init__(self, object: typing.Any, string: str, string2: str): ...
    @typing.overload
    def __init__(self, object: typing.Any, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...

class TooManyIterationsException(ThermoException):
    @typing.overload
    def __init__(self, object: typing.Any, string: str, long: int): ...
    @typing.overload
    def __init__(self, string: str, string2: str, long: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.util.exception")``.

    InvalidInputException: typing.Type[InvalidInputException]
    IsNaNException: typing.Type[IsNaNException]
    NotInitializedException: typing.Type[NotInitializedException]
    ThermoException: typing.Type[ThermoException]
    TooManyIterationsException: typing.Type[TooManyIterationsException]
