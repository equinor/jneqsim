
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.PVTsimulation.modelTuning
import jneqsim.neqsim.PVTsimulation.reservoirProperties
import jneqsim.neqsim.PVTsimulation.simulation
import jneqsim.neqsim.PVTsimulation.util
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.PVTsimulation")``.

    modelTuning: jneqsim.neqsim.PVTsimulation.modelTuning.__module_protocol__
    reservoirProperties: jneqsim.neqsim.PVTsimulation.reservoirProperties.__module_protocol__
    simulation: jneqsim.neqsim.PVTsimulation.simulation.__module_protocol__
    util: jneqsim.neqsim.PVTsimulation.util.__module_protocol__
