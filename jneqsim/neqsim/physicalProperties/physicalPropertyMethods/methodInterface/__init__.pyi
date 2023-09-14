
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jneqsim.neqsim.physicalProperties.physicalPropertyMethods
import jneqsim.neqsim.thermo
import typing



class ConductivityInterface(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethodInterface):
    def calcConductivity(self) -> float: ...
    def clone(self) -> 'ConductivityInterface': ...

class DensityInterface(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethodInterface):
    def calcDensity(self) -> float: ...
    def clone(self) -> 'DensityInterface': ...

class DiffusivityInterface(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface, jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethodInterface):
    def calcBinaryDiffusionCoefficient(self, int: int, int2: int, int3: int) -> float: ...
    def calcDiffusionCoefficients(self, int: int, int2: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def calcEffectiveDiffusionCoefficients(self) -> None: ...
    def clone(self) -> 'DiffusivityInterface': ...
    def getEffectiveDiffusionCoefficient(self, int: int) -> float: ...
    def getFickBinaryDiffusionCoefficient(self, int: int, int2: int) -> float: ...
    def getMaxwellStefanBinaryDiffusionCoefficient(self, int: int, int2: int) -> float: ...

class ViscosityInterface(jneqsim.neqsim.physicalProperties.physicalPropertyMethods.PhysicalPropertyMethodInterface):
    def calcViscosity(self) -> float: ...
    def clone(self) -> 'ViscosityInterface': ...
    def getPureComponentViscosity(self, int: int) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.physicalProperties.physicalPropertyMethods.methodInterface")``.

    ConductivityInterface: typing.Type[ConductivityInterface]
    DensityInterface: typing.Type[DensityInterface]
    DiffusivityInterface: typing.Type[DiffusivityInterface]
    ViscosityInterface: typing.Type[ViscosityInterface]