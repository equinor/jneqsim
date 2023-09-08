
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.processSimulation.mechanicalDesign
import jneqsim.neqsim.processSimulation.processEquipment
import typing



class AdsorberMechanicalDesign(jneqsim.neqsim.processSimulation.mechanicalDesign.MechanicalDesign):
    def __init__(self, processEquipmentInterface: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface): ...
    def calcDesign(self) -> None: ...
    def getOuterDiameter(self) -> float: ...
    def getWallThickness(self) -> float: ...
    def readDesignSpecifications(self) -> None: ...
    def setDesign(self) -> None: ...
    def setOuterDiameter(self, double: float) -> None: ...
    def setWallThickness(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.mechanicalDesign.adsorber")``.

    AdsorberMechanicalDesign: typing.Type[AdsorberMechanicalDesign]
