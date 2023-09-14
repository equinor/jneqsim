
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import typing



class DataSmoothor:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, int3: int, int4: int): ...
    def findCoefs(self) -> None: ...
    def getSmoothedNumbers(self) -> typing.MutableSequence[float]: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def runSmoothing(self) -> None: ...
    def setSmoothedNumbers(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.dataAnalysis.dataSmoothing")``.

    DataSmoothor: typing.Type[DataSmoothor]
