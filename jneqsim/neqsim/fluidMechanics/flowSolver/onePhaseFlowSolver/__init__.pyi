
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSolver
import jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver.onePhasePipeFlowSolver
import typing



class OnePhaseFlowSolver(jneqsim.neqsim.fluidMechanics.flowSolver.FlowSolver):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver")``.

    OnePhaseFlowSolver: typing.Type[OnePhaseFlowSolver]
    onePhasePipeFlowSolver: jneqsim.neqsim.fluidMechanics.flowSolver.onePhaseFlowSolver.onePhasePipeFlowSolver.__module_protocol__
