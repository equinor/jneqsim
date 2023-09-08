import os

from jneqsim import neqsim



def do_depressurize_gas():
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

    assert inlet_fluid.getTemperature("C") < 10.0

print (os.path.dirname(os.path.abspath(__file__)))

neqsim.thermo.system.SystemSrkEos()
neqsim.api.ioc.CalculationResult()

neqsim.thermo.system.SystemSrkEos().setPressure(double=2)
neqsim.api.ioc.CalculationResult()
do_depressurize_gas()

