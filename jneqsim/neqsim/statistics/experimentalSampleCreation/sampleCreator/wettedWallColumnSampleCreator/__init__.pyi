
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator
import typing



class WettedWallColumnSampleCreator(jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator.SampleCreator):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def calcdPdt(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def setSampleValues(self) -> None: ...
    def smoothData(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator.wettedWallColumnSampleCreator")``.

    WettedWallColumnSampleCreator: typing.Type[WettedWallColumnSampleCreator]
