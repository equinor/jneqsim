
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import jneqsim.neqsim.thermo
import jneqsim.neqsim.thermo.component
import jneqsim.neqsim.thermo.phase
import typing



class Element(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface):
    def __init__(self, string: str): ...
    @staticmethod
    def getAllElementComponentNames() -> java.util.ArrayList[str]: ...
    def getElementCoefs(self) -> typing.MutableSequence[float]: ...
    def getElementNames(self) -> typing.MutableSequence[str]: ...
    def getName(self) -> str: ...
    def getNumberOfElements(self, string: str) -> float: ...

class UNIFACgroup(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface, java.lang.Comparable['UNIFACgroup']):
    QMixdN: typing.MutableSequence[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    def calcQComp(self, componentGEUnifac: jneqsim.neqsim.thermo.component.ComponentGEUnifac) -> float: ...
    def calcQMix(self, phaseGEUnifac: jneqsim.neqsim.thermo.phase.PhaseGEUnifac) -> float: ...
    def calcQMixdN(self, phaseGEUnifac: jneqsim.neqsim.thermo.phase.PhaseGEUnifac) -> typing.MutableSequence[float]: ...
    def calcXComp(self, componentGEUnifac: jneqsim.neqsim.thermo.component.ComponentGEUnifac) -> float: ...
    def compareTo(self, uNIFACgroup: 'UNIFACgroup') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getGroupIndex(self) -> int: ...
    def getGroupName(self) -> str: ...
    def getLnGammaComp(self) -> float: ...
    def getLnGammaCompdT(self) -> float: ...
    def getLnGammaCompdTdT(self) -> float: ...
    def getLnGammaMix(self) -> float: ...
    def getLnGammaMixdT(self) -> float: ...
    def getLnGammaMixdTdT(self) -> float: ...
    def getLnGammaMixdn(self, int: int) -> float: ...
    def getMainGroup(self) -> int: ...
    def getN(self) -> int: ...
    def getQ(self) -> float: ...
    def getQComp(self) -> float: ...
    def getQMix(self) -> float: ...
    @typing.overload
    def getQMixdN(self, int: int) -> float: ...
    @typing.overload
    def getQMixdN(self) -> typing.MutableSequence[float]: ...
    def getR(self) -> float: ...
    def getSubGroup(self) -> int: ...
    def getXComp(self) -> float: ...
    def hashCode(self) -> int: ...
    def setGroupIndex(self, int: int) -> None: ...
    def setGroupName(self, string: str) -> None: ...
    def setLnGammaComp(self, double: float) -> None: ...
    def setLnGammaCompdT(self, double: float) -> None: ...
    def setLnGammaCompdTdT(self, double: float) -> None: ...
    def setLnGammaMix(self, double: float) -> None: ...
    def setLnGammaMixdT(self, double: float) -> None: ...
    def setLnGammaMixdTdT(self, double: float) -> None: ...
    def setLnGammaMixdn(self, double: float, int: int) -> None: ...
    def setMainGroup(self, int: int) -> None: ...
    def setN(self, int: int) -> None: ...
    def setQ(self, double: float) -> None: ...
    def setQComp(self, double: float) -> None: ...
    def setQMix(self, double: float) -> None: ...
    def setQMixdN(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def setR(self, double: float) -> None: ...
    def setSubGroup(self, int: int) -> None: ...
    def setXComp(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.thermo.atomElement")``.

    Element: typing.Type[Element]
    UNIFACgroup: typing.Type[UNIFACgroup]
