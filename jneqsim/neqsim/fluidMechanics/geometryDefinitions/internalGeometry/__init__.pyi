
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.fluidMechanics.geometryDefinitions.internalGeometry.packings
import jneqsim.neqsim.fluidMechanics.geometryDefinitions.internalGeometry.wall
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.fluidMechanics.geometryDefinitions.internalGeometry")``.

    packings: jneqsim.neqsim.fluidMechanics.geometryDefinitions.internalGeometry.packings.__module_protocol__
    wall: jneqsim.neqsim.fluidMechanics.geometryDefinitions.internalGeometry.wall.__module_protocol__
