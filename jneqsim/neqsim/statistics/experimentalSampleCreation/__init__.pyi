
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.statistics.experimentalSampleCreation.readDataFromFile
import jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.statistics.experimentalSampleCreation")``.

    readDataFromFile: jneqsim.neqsim.statistics.experimentalSampleCreation.readDataFromFile.__module_protocol__
    sampleCreator: jneqsim.neqsim.statistics.experimentalSampleCreation.sampleCreator.__module_protocol__
