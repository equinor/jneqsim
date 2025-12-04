# jNeqSim

[![PyPI version](https://img.shields.io/pypi/v/jneqsim.svg)](https://pypi.org/project/jneqsim/)
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

## Version Management

jneqsim uses a controlled release process to ensure compatibility:

- **Pinned Versions**: Each jneqsim release is pinned to a specific, tested NeqSim JAR version
- **Automated Updates**: The nightly CI workflow automatically checks for new NeqSim releases and publishes updated jneqsim packages when available
- **No Auto-Updates**: Applications using jneqsim will not automatically download newer NeqSim versions - they use the tested version that comes with their installed jneqsim package
- **Cache Management**: Downloaded JARs are cached locally in `~/.jneqsim/cache` for faster subsequent usage

## Development

### Running Tests

The project uses pytest with custom markers to categorize tests. Test dependencies are already included in the development dependencies.

```bash
# Install development dependencies (includes pytest and pytest-mock)
pip install -e ".[dev]"
# or if using poetry: poetry install

# Run unit tests (fast, excludes tests marked as slow)
pytest -v -m "not slow" tests/

# Run all tests (may download JARs for integration tests)
pytest -v tests/

# Run with coverage (requires pytest-cov)
pip install pytest-cov
pytest --cov=jneqsim --cov-report=html tests/
```

**Test markers:**
- `slow`: Tests that may download files or take longer to run
- `integration`: Integration tests that require external dependencies
- `unit`: Fast unit tests (default)


<a id="Contributing"></a>

## :+1: Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
