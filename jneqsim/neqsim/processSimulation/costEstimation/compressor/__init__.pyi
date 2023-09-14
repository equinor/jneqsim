
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.processSimulation.costEstimation
import jneqsim.neqsim.processSimulation.mechanicalDesign.compressor
import typing



class CompressorCostEstimate(jneqsim.neqsim.processSimulation.costEstimation.UnitCostEstimateBaseClass):
    def __init__(self, compressorMechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.compressor.CompressorMechanicalDesign): ...
    def getTotaltCost(self) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.costEstimation.compressor")``.

    CompressorCostEstimate: typing.Type[CompressorCostEstimate]
