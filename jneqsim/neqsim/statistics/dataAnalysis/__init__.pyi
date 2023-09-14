
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.statistics.dataAnalysis.dataSmoothing
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.dataAnalysis")``.

    dataSmoothing: jneqsim.neqsim.statistics.dataAnalysis.dataSmoothing.__module_protocol__
