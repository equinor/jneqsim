
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.processSimulation.costEstimation
import jneqsim.neqsim.processSimulation.mechanicalDesign.separator
import typing



class SeparatorCostEstimate(jneqsim.neqsim.processSimulation.costEstimation.UnitCostEstimateBaseClass):
    def __init__(self, separatorMechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.separator.SeparatorMechanicalDesign): ...
    def getTotaltCost(self) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.costEstimation.separator")``.

    SeparatorCostEstimate: typing.Type[SeparatorCostEstimate]
