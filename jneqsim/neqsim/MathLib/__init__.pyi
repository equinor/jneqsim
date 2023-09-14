
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.MathLib.generalMath
import jneqsim.neqsim.MathLib.nonLinearSolver
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.MathLib")``.

    generalMath: jneqsim.neqsim.MathLib.generalMath.__module_protocol__
    nonLinearSolver: jneqsim.neqsim.MathLib.nonLinearSolver.__module_protocol__
