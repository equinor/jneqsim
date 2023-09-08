
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import Jama
import java.util
import jpype
import jneqsim.neqsim.thermo
import jneqsim.neqsim.thermo.component
import jneqsim.neqsim.thermo.phase
import jneqsim.neqsim.thermo.system
import jneqsim.neqsim.util
import typing



class ChemicalReaction(jneqsim.neqsim.util.NamedBaseClass, jneqsim.neqsim.thermo.ThermodynamicConstantsInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray], doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float, double4: float, double5: float): ...
    def calcK(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, int: int) -> float: ...
    def calcKgamma(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, int: int) -> float: ...
    def calcKx(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, int: int) -> float: ...
    def checkK(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface) -> None: ...
    def getActivationEnergy(self) -> float: ...
    @typing.overload
    def getK(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> float: ...
    @typing.overload
    def getK(self) -> typing.MutableSequence[float]: ...
    def getNames(self) -> typing.MutableSequence[str]: ...
    def getProductNames(self) -> typing.MutableSequence[str]: ...
    @typing.overload
    def getRateFactor(self) -> float: ...
    @typing.overload
    def getRateFactor(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> float: ...
    def getReactantNames(self) -> typing.MutableSequence[str]: ...
    def getReactionHeat(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> float: ...
    def getSaturationRatio(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface, int: int) -> float: ...
    def getStocCoefs(self) -> typing.MutableSequence[float]: ...
    def init(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> None: ...
    def initMoleNumbers(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, componentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.thermo.component.ComponentInterface], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def reactantsContains(self, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> bool: ...
    def setActivationEnergy(self, double: float) -> None: ...
    @typing.overload
    def setK(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def setK(self, int: int, double: float) -> None: ...
    def setRateFactor(self, double: float) -> None: ...

class ChemicalReactionFactory:
    @staticmethod
    def getChemicalReaction(string: str) -> ChemicalReaction: ...
    @staticmethod
    def getChemicalReactionNames() -> typing.MutableSequence[str]: ...

class ChemicalReactionList(jneqsim.neqsim.thermo.ThermodynamicConstantsInterface):
    def __init__(self): ...
    def calcReacMatrix(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> None: ...
    def calcReacRates(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, componentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.thermo.component.ComponentInterface], jpype.JArray]) -> Jama.Matrix: ...
    def calcReferencePotentials(self) -> typing.MutableSequence[float]: ...
    def checkReactions(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface) -> None: ...
    def createReactionMatrix(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, componentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.thermo.component.ComponentInterface], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getAllComponents(self) -> typing.MutableSequence[str]: ...
    def getChemicalReactionList(self) -> java.util.ArrayList[ChemicalReaction]: ...
    def getReacMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getReaction(self, int: int) -> ChemicalReaction: ...
    @typing.overload
    def getReaction(self, string: str) -> ChemicalReaction: ...
    def getReactionGMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getReactionMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getStocMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def initMoleNumbers(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, componentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.thermo.component.ComponentInterface], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def reacHeat(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, string: str) -> float: ...
    def readReactions(self, systemInterface: jneqsim.neqsim.thermo.system.SystemInterface) -> None: ...
    def removeJunkReactions(self, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def setChemicalReactionList(self, arrayList: java.util.ArrayList[ChemicalReaction]) -> None: ...
    def updateReferencePotentials(self, phaseInterface: jneqsim.neqsim.thermo.phase.PhaseInterface, componentInterfaceArray: typing.Union[typing.List[jneqsim.neqsim.thermo.component.ComponentInterface], jpype.JArray]) -> typing.MutableSequence[float]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.chemicalReactions.chemicalReaction")``.

    ChemicalReaction: typing.Type[ChemicalReaction]
    ChemicalReactionFactory: typing.Type[ChemicalReactionFactory]
    ChemicalReactionList: typing.Type[ChemicalReactionList]
