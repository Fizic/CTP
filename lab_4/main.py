import math
import matplotlib.pyplot as plt


def plot_by_function(function) -> None:
    times = [time / 1000000 for time in range(100)]
    values = [function(time) for time in times]
    plt.grid(True)
    plt.plot(times, values)
    plt.show()


class OscillatoryCircuit:
    def __init__(self, R: float, L: float, C: float):
        self.R = R
        self.L = L
        self.C = C
        self.omega = self.get_omega()

    def get_omega(self):
        return 1 / math.sqrt(self.L * self.C)

    def get_q_by_t(self, t: float) -> float:
        return self.C * (1 - math.cos(self.omega * t))

    def get_amperage_by_t(self, t: float) -> float:
        return -self.C * self.omega * math.sin(self.omega * t)

    def get_voltage_by_t(self, t: float) -> float:
        return self.get_q_by_t(t) / self.C

    def plot_q_versus_time(self) -> None:
        plot_by_function(self.get_q_by_t)

    def plot_amperage_versus_time(self) -> None:
        plot_by_function(self.get_amperage_by_t)

    def plot_voltage_versus_time(self) -> None:
        plot_by_function(self.get_voltage_by_t)


oscillatory_circuit = OscillatoryCircuit(1, 2e-6, 8e-10)
oscillatory_circuit.plot_q_versus_time()
oscillatory_circuit.plot_amperage_versus_time()
oscillatory_circuit.plot_voltage_versus_time()
