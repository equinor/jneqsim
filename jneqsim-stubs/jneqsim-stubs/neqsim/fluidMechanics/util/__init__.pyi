
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization
import jneqsim.neqsim.fluidMechanics.util.timeSeries
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util")``.

    fluidMechanicsDataHandeling: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsDataHandeling.__module_protocol__
    fluidMechanicsVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.__module_protocol__
    timeSeries: jneqsim.neqsim.fluidMechanics.util.timeSeries.__module_protocol__
