
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSolver.twoPhaseFlowSolver.stirredCellSolver
import jneqsim.neqsim.fluidMechanics.flowSolver.twoPhaseFlowSolver.twoPhasePipeFlowSolver
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSolver.twoPhaseFlowSolver")``.

    stirredCellSolver: jneqsim.neqsim.fluidMechanics.flowSolver.twoPhaseFlowSolver.stirredCellSolver.__module_protocol__
    twoPhasePipeFlowSolver: jneqsim.neqsim.fluidMechanics.flowSolver.twoPhaseFlowSolver.twoPhasePipeFlowSolver.__module_protocol__
