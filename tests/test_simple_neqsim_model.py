import pytest

from jneqsim import neqsim


def test_pressurize_gas():
    if neqsim is None:
        pytest.skip("NeqSim JVM not initialized - JPype may not be available")

    inlet_fluid = neqsim.thermo.system.SystemSrkEos()
    thermo_ops = neqsim.thermodynamicoperations.ThermodynamicOperations(inlet_fluid)
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

    assert inlet_fluid.getTemperature("C") < 10.0
