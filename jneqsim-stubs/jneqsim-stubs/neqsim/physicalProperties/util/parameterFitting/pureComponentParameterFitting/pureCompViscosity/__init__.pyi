
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity.chungMethod
import jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity.linearLiquidModel
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity")``.

    chungMethod: jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity.chungMethod.__module_protocol__
    linearLiquidModel: jneqsim.neqsim.physicalProperties.util.parameterFitting.pureComponentParameterFitting.pureCompViscosity.linearLiquidModel.__module_protocol__
