
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.statistics.experimentalEquipmentData
import jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator.wettedWallColumnSampleCreator
import jneqsim.neqsim.thermo.system
import jneqsim.neqsim.thermodynamicOperations
import typing



class SampleCreator:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, thermodynamicOperations: jneqsim.neqsim.thermodynamicOperations.ThermodynamicOperations): ...
    def setExperimentalEquipment(self, experimentalEquipmentData: jneqsim.neqsim.statistics.experimentalEquipmentData.ExperimentalEquipmentData) -> None: ...
    def setThermoSystem(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator")``.

    SampleCreator: typing.Type[SampleCreator]
    wettedWallColumnSampleCreator: jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator.wettedWallColumnSampleCreator.__module_protocol__
