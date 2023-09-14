
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.processSimulation.mechanicalDesign
import jneqsim.neqsim.processSimulation.processEquipment
import typing



class ValveMechanicalDesign(jneqsim.neqsim.processSimulation.mechanicalDesign.MechanicalDesign):
    def __init__(self, processEquipmentInterface: jneqsim.neqsim.processSimulation.processEquipment.ProcessEquipmentInterface): ...
    def calcDesign(self) -> None: ...
    def displayResults(self) -> None: ...
    def readDesignSpecifications(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.mechanicalDesign.valve")``.

    ValveMechanicalDesign: typing.Type[ValveMechanicalDesign]
