
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization
import jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization")``.

    flowNodeVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowNodeVisualization.__module_protocol__
    flowSystemVisualization: jneqsim.neqsim.fluidMechanics.util.fluidMechanicsVisualization.flowSystemVisualization.__module_protocol__
