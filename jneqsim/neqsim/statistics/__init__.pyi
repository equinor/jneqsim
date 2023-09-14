
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.statistics.dataAnalysis
import jneqsim.neqsim.statistics.experimentalEquipmentData
import jneqsim.neqsim.statistics.experimentalSampleCreation
import jneqsim.neqsim.statistics.monteCarloSimulation
import jneqsim.neqsim.statistics.parameterFitting
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics")``.

    dataAnalysis: jneqsim.neqsim.statistics.dataAnalysis.__module_protocol__
    experimentalEquipmentData: jneqsim.neqsim.statistics.experimentalEquipmentData.__module_protocol__
    experimentalSampleCreation: jneqsim.neqsim.statistics.experimentalSampleCreation.__module_protocol__
    monteCarloSimulation: jneqsim.neqsim.statistics.monteCarloSimulation.__module_protocol__
    parameterFitting: jneqsim.neqsim.statistics.parameterFitting.__module_protocol__
