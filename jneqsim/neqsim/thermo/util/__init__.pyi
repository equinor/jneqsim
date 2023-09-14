
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.thermo.util.GERG
import jneqsim.neqsim.thermo.util.JNI
import jneqsim.neqsim.thermo.util.benchmark
import jneqsim.neqsim.thermo.util.constants
import jneqsim.neqsim.thermo.util.empiric
import jneqsim.neqsim.thermo.util.readwrite
import jneqsim.neqsim.thermo.util.referenceEquations
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermo.util")``.

    GERG: jneqsim.neqsim.thermo.util.GERG.__module_protocol__
    JNI: jneqsim.neqsim.thermo.util.JNI.__module_protocol__
    benchmark: jneqsim.neqsim.thermo.util.benchmark.__module_protocol__
    constants: jneqsim.neqsim.thermo.util.constants.__module_protocol__
    empiric: jneqsim.neqsim.thermo.util.empiric.__module_protocol__
    readwrite: jneqsim.neqsim.thermo.util.readwrite.__module_protocol__
    referenceEquations: jneqsim.neqsim.thermo.util.referenceEquations.__module_protocol__
