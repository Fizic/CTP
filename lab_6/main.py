import matplotlib.pyplot as plt


class DCSource:
    def __init__(self, voltage: float, r: float):
        self.voltage = voltage
        self.r = r


class Rheostat:
    def __init__(self, r: float, min_r: float, max_r: float):
        self.r = r
        self.min_r = min_r
        self.max_r = max_r

    def change_resistance(self, r: float) -> None:
        self.r = r


class ElectricalCircuit:
    def __init__(self, dc_source: DCSource, rheostat: Rheostat):
        self.dc_source = dc_source
        self.rheostat = rheostat

    def get_amperage(self) -> float:
        return self.dc_source.voltage / (self.rheostat.r + self.dc_source.r)

    def get_max_amperage(self) -> float:
        return self.dc_source.voltage / (self.rheostat.min_r + self.dc_source.r)

    def get_voltage(self) -> float:
        return self.dc_source.voltage * (1 - self.get_amperage() / self.get_max_amperage())

    def get_full_power(self) -> float:
        return self.dc_source.voltage * self.get_amperage()

    def get_power(self) -> float:
        return self.get_voltage() * self.get_amperage()

    def get_efficiency(self) -> float:
        return self.get_power() / self.get_full_power()

    def plot_voltage_versus_amperage(self) -> None:
        amperages = []
        voltages = []
        for r in range(int(self.rheostat.min_r * 100), int(self.rheostat.max_r * 100)):
            self.rheostat.change_resistance(r / 100)
            amperages.append(self.get_amperage())
            voltages.append(self.get_voltage())
        plt.grid(True)
        plt.plot(amperages, voltages)
        plt.show()

    def plot_power_versus_amperage(self) -> None:
        amperages = []
        powers = []
        full_powers = []
        for r in range(int(self.rheostat.min_r * 100), int(self.rheostat.max_r * 100)):
            self.rheostat.change_resistance(r / 100)
            amperages.append(self.get_amperage())
            powers.append(self.get_power())
            full_powers.append(self.get_full_power())
        plt.grid(True)
        plt.plot(amperages, powers)
        plt.plot(amperages, full_powers)
        plt.show()

    def plot_efficiency_versus_amperage(self) -> None:
        amperages = []
        efficiencyes = []
        for r in range(int(self.rheostat.min_r * 100), int(self.rheostat.max_r * 100)):
            self.rheostat.change_resistance(r / 100)
            amperages.append(self.get_amperage())
            efficiencyes.append(self.get_efficiency())
        plt.grid(True)
        plt.plot(amperages, efficiencyes)
        plt.show()


dc_source = DCSource(12, 0.1)
rheostat = Rheostat(1, 0, 10)
electrical_circuit = ElectricalCircuit(dc_source, rheostat)
electrical_circuit.plot_voltage_versus_amperage()
electrical_circuit.plot_power_versus_amperage()
electrical_circuit.plot_efficiency_versus_amperage()
