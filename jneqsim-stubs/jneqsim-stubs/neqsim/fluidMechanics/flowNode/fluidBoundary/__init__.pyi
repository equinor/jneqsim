
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc
import jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary")``.

    heatMassTransferCalc: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.heatMassTransferCalc.__module_protocol__
    interphaseTransportCoefficient: jneqsim.neqsim.fluidMechanics.flowNode.fluidBoundary.interphaseTransportCoefficient.__module_protocol__
