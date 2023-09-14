
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import jneqsim.neqsim.statistics.experimentalSampleCreation.readDataFromFile.wettedWallColumnReader
import typing



class DataObjectInterface: ...

class DataReaderInterface:
    def readData(self) -> None: ...

class DataObject(DataObjectInterface):
    def __init__(self): ...

class DataReader(DataReaderInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getSampleObjectList(self) -> java.util.ArrayList[DataObject]: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def readData(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.experimentalSampleCreation.readDataFromFile")``.

    DataObject: typing.Type[DataObject]
    DataObjectInterface: typing.Type[DataObjectInterface]
    DataReader: typing.Type[DataReader]
    DataReaderInterface: typing.Type[DataReaderInterface]
    wettedWallColumnReader: jneqsim.neqsim.statistics.experimentalSampleCreation.readDataFromFile.wettedWallColumnReader.__module_protocol__
