
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.processSimulation.costEstimation
import jneqsim.neqsim.processSimulation.mechanicalDesign.valve
import typing



class ValveCostEstimate(jneqsim.neqsim.processSimulation.costEstimation.UnitCostEstimateBaseClass):
    def __init__(self, valveMechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.valve.ValveMechanicalDesign): ...
    def getTotaltCost(self) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.costEstimation.valve")``.

    ValveCostEstimate: typing.Type[ValveCostEstimate]
