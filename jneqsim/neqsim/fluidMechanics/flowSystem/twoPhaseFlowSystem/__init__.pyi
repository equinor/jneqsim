
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSystem
import jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.shipSystem
import jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.stirredCellSystem
import jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.twoPhasePipeFlowSystem
import jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.twoPhaseReactorFlowSystem
import jneqsim.neqsim.fluidMechanics.geometryDefinitions.pipe
import jneqsim.neqsim.thermo.system
import typing



class TwoPhaseFlowSystem(jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystem):
    pipe: jneqsim.neqsim.fluidMechanics.geometryDefinitions.pipe.PipeData = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem")``.

    TwoPhaseFlowSystem: typing.Type[TwoPhaseFlowSystem]
    shipSystem: jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.shipSystem.__module_protocol__
    stirredCellSystem: jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.stirredCellSystem.__module_protocol__
    twoPhasePipeFlowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.twoPhasePipeFlowSystem.__module_protocol__
    twoPhaseReactorFlowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.twoPhaseFlowSystem.twoPhaseReactorFlowSystem.__module_protocol__
