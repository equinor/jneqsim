
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompInterfaceTension
import jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting")``.

    pureCompInterfaceTension: jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompInterfaceTension.__module_protocol__
    pureCompViscosity: jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity.__module_protocol__
