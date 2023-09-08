
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowLeg
import jneqsim.neqsim.fluidMechanics.flowNode
import jneqsim.neqsim.fluidMechanics.flowSolver
import jneqsim.neqsim.fluidMechanics.flowSystem
import jneqsim.neqsim.fluidMechanics.geometryDefinitions
import jneqsim.neqsim.fluidMechanics.util
import typing



class fluidMech:
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics")``.

    fluidMech: typing.Type[fluidMech]
    flowLeg: jneqsim.neqsim.fluidMechanics.flowLeg.__module_protocol__
    flowNode: jneqsim.neqsim.fluidMechanics.flowNode.__module_protocol__
    flowSolver: jneqsim.neqsim.fluidMechanics.flowSolver.__module_protocol__
    flowSystem: jneqsim.neqsim.fluidMechanics.flowSystem.__module_protocol__
    geometryDefinitions: jneqsim.neqsim.fluidMechanics.geometryDefinitions.__module_protocol__
    util: jneqsim.neqsim.fluidMechanics.util.__module_protocol__
