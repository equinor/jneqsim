# jNeqSim

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Python interface for the [NeqSim java package](https://equinor.github.io/neqsimhome/), with stubs. Java interface is created with [jpype](https://jpype.readthedocs.io/en/latest/index.html#), and stubs are generated with [stubgenj](https://gitlab.cern.ch/scripting-tools/stubgenj)


## PYPI

[https://pypi.org/project/jneqsim/](https://pypi.org/project/jneqsim/)
> [!NOTE]
> JNeqSim mirrors NeqSims versions

## Demo

![demo.gif](docs/demo.gif)


## Example

```python
from jneqsim import neqsim


def pressurize_gas():
    inlet_fluid = neqsim.thermo.system.SystemSrkEos()
    neqsim.thermo.system.SystemSrkEos()
    thermo_ops = neqsim.thermodynamicOperations.ThermodynamicOperations(inlet_fluid)
    inlet_fluid.addComponent("methane", 100.0)

    inlet_fluid.setTemperature(10, "C")
    inlet_fluid.setPressure(20, "bara")
    inlet_fluid.setMultiPhaseCheck(True)
    inlet_fluid.setSolidPhaseCheck("methane")

    thermo_ops.TPflash()
    thermo_ops.bubblePointTemperatureFlash()

    inlet_fluid.initProperties()
    enthalpy = inlet_fluid.getEnthalpy()

    inlet_fluid.setPressure(1.0, "bara")
    thermo_ops.PHflash(enthalpy)
```

## Dependencies

- [jpype](https://jpype.readthedocs.io/en/latest/index.html#)


<a id="Contributing"></a>

## :+1: Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
