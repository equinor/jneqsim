
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.MathLib
import jneqsim.neqsim.PVTsimulation
import jneqsim.neqsim.api
import jneqsim.neqsim.chemicalReactions
import jneqsim.neqsim.dataPresentation
import jneqsim.neqsim.fluidMechanics
import jneqsim.neqsim.physicalProperties
import jneqsim.neqsim.processSimulation
import jneqsim.neqsim.standards
import jneqsim.neqsim.statistics
import jneqsim.neqsim.thermo
import jneqsim.neqsim.thermodynamicOperations
import jneqsim.neqsim.util
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("neqsim")``.

    MathLib: jneqsim.neqsim.MathLib.__module_protocol__
    PVTsimulation: jneqsim.neqsim.PVTsimulation.__module_protocol__
    api: jneqsim.neqsim.api.__module_protocol__
    chemicalReactions: jneqsim.neqsim.chemicalReactions.__module_protocol__
    dataPresentation: jneqsim.neqsim.dataPresentation.__module_protocol__
    fluidMechanics: jneqsim.neqsim.fluidMechanics.__module_protocol__
    physicalProperties: jneqsim.neqsim.physicalProperties.__module_protocol__
    processSimulation: jneqsim.neqsim.processSimulation.__module_protocol__
    standards: jneqsim.neqsim.standards.__module_protocol__
    statistics: jneqsim.neqsim.statistics.__module_protocol__
    thermo: jneqsim.neqsim.thermo.__module_protocol__
    thermodynamicOperations: jneqsim.neqsim.thermodynamicOperations.__module_protocol__
    util: jneqsim.neqsim.util.__module_protocol__
