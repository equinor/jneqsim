
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jneqsim.neqsim.processSimulation.costEstimation.compressor
import jneqsim.neqsim.processSimulation.costEstimation.separator
import jneqsim.neqsim.processSimulation.costEstimation.valve
import jneqsim.neqsim.processSimulation.mechanicalDesign
import typing



class CostEstimateBaseClass(java.io.Serializable):
    @typing.overload
    def __init__(self, systemMechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.SystemMechanicalDesign): ...
    @typing.overload
    def __init__(self, systemMechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.SystemMechanicalDesign, double: float): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCAPEXestimate(self) -> float: ...
    def getWeightBasedCAPEXEstimate(self) -> float: ...
    def hashCode(self) -> int: ...

class UnitCostEstimateBaseClass(java.io.Serializable):
    mechanicalEquipment: jneqsim.neqsim.processSimulation.mechanicalDesign.MechanicalDesign = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mechanicalDesign: jneqsim.neqsim.processSimulation.mechanicalDesign.MechanicalDesign): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getTotaltCost(self) -> float: ...
    def hashCode(self) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.costEstimation")``.

    CostEstimateBaseClass: typing.Type[CostEstimateBaseClass]
    UnitCostEstimateBaseClass: typing.Type[UnitCostEstimateBaseClass]
    compressor: jneqsim.neqsim.processSimulation.costEstimation.compressor.__module_protocol__
    separator: jneqsim.neqsim.processSimulation.costEstimation.separator.__module_protocol__
    valve: jneqsim.neqsim.processSimulation.costEstimation.valve.__module_protocol__
