
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import jneqsim.neqsim.processSimulation.processEquipment
import jneqsim.neqsim.processSimulation.processEquipment.stream
import typing



class Manifold(jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentBaseClass):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def addStream(self, streamInterface: jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface) -> None: ...
    def getMixedStream(self) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    def getSplitStream(self, int: int) -> jneqsim.neqsim.processSimulation.processEquipment.stream.StreamInterface: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    def setSplitFactors(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.processEquipment.manifold")``.

    Manifold: typing.Type[Manifold]
