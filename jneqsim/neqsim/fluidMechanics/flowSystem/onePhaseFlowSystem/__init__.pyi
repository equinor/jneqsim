
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowSystem
import jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem.pipeFlowSystem
import jneqsim.neqsim.fluidMechanics.geometryDefinitions.pipe
import jneqsim.neqsim.thermo.system
import typing



class OnePhaseFlowSystem(jneqsim.neqsim.fluidMechanics.flowSystem.FlowSystem):
    pipe: jneqsim.neqsim.fluidMechanics.geometryDefinitions.pipe.PipeData = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem")``.

    OnePhaseFlowSystem: typing.Type[OnePhaseFlowSystem]
    pipeFlowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.onePhaseFlowSystem.pipeFlowSystem.__module_protocol__
