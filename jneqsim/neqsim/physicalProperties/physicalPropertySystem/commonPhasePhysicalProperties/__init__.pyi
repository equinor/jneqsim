
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertySystem
import jneqsim.neqsim.thermo.phase
import typing



class DefaultPhysicalProperties(jneqsim.neqsim.physicalProperties.physicalPropertySystem.PhysicalProperties):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, int: int, int2: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertySystem.commonPhasePhysicalProperties")``.

    DefaultPhysicalProperties: typing.Type[DefaultPhysicalProperties]
