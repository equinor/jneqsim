
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.dataPresentation.fileHandeling.createTextFile
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.dataPresentation.fileHandeling")``.

    createTextFile: jneqsim.neqsim.dataPresentation.fileHandeling.createTextFile.__module_protocol__
