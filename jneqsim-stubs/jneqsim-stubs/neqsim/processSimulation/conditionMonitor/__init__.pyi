
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import jneqsim.neqsim.processSimulation.processSystem
import typing



class ConditionMonitor(java.io.Serializable, java.lang.Runnable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, processSystem: jneqsim.neqsim.processSimulation.processSystem.ProcessSystem): ...
    @typing.overload
    def conditionAnalysis(self) -> None: ...
    @typing.overload
    def conditionAnalysis(self, string: str) -> None: ...
    def getProcess(self) -> jneqsim.neqsim.processSimulation.processSystem.ProcessSystem: ...
    def getReport(self) -> str: ...
    def run(self) -> None: ...

class ConditionMonitorSpecifications(java.io.Serializable):
    HXmaxDeltaT: typing.ClassVar[float] = ...
    HXmaxDeltaT_ErrorMsg: typing.ClassVar[str] = ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processSimulation.conditionMonitor")``.

    ConditionMonitor: typing.Type[ConditionMonitor]
    ConditionMonitorSpecifications: typing.Type[ConditionMonitorSpecifications]
