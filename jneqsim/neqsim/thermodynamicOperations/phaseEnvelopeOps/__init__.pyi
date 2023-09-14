
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.thermodynamicOperations.phaseEnvelopeOps.multicomponentEnvelopeOps
import jneqsim.neqsim.thermodynamicOperations.phaseEnvelopeOps.reactiveCurves
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermodynamicOperations.phaseEnvelopeOps")``.

    multicomponentEnvelopeOps: jneqsim.neqsim.thermodynamicOperations.phaseEnvelopeOps.multicomponentEnvelopeOps.__module_protocol__
    reactiveCurves: jneqsim.neqsim.thermodynamicOperations.phaseEnvelopeOps.reactiveCurves.__module_protocol__
