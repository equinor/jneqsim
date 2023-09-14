
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.awt.image
import javax.swing
import jpype
import org.jfree.chart
import org.jfree.data.category
import typing



class graph2b(javax.swing.JFrame):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], stringArray: typing.Union[typing.List[str], jpype.JArray], string2: str, string3: str, string4: str): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], stringArray: typing.Union[typing.List[str], jpype.JArray], string2: str, string3: str, string4: str): ...
    def createCategoryDataSource(self) -> org.jfree.data.category.CategoryDataset: ...
    def getBufferedImage(self) -> java.awt.image.BufferedImage: ...
    def getChart(self) -> org.jfree.chart.JFreeChart: ...
    def getChartPanel(self) -> org.jfree.chart.ChartPanel: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def saveFigure(self, string: str) -> None: ...
    def setChart(self, jFreeChart: org.jfree.chart.JFreeChart) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.dataPresentation.JFreeChart")``.

    graph2b: typing.Type[graph2b]
