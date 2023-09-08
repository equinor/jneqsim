
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundaryNode.fluidBoundaryNonReactiveNode
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundaryNode.fluidBoundaryReactiveNode
import jneqsim.neqsim.thermo.system
import typing



class FluidBoundaryNodeInterface:
    def getBulkSystem(self) -> jneqsim.neqsim.thermo.system.SystemInterface: ...

class FluidBoundaryNode(FluidBoundaryNodeInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface): ...
    def getBulkSystem(self) -> jneqsim.neqsim.thermo.system.SystemInterface: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundaryNode")``.

    FluidBoundaryNode: typing.Type[FluidBoundaryNode]
    FluidBoundaryNodeInterface: typing.Type[FluidBoundaryNodeInterface]
    fluidBoundaryNonReactiveNode: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundaryNode.fluidBoundaryNonReactiveNode.__module_protocol__
    fluidBoundaryReactiveNode: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.finiteVolumeBoundary.fluidBoundaryNode.fluidBoundaryReactiveNode.__module_protocol__
