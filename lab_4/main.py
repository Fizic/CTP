import math
import matplotlib.pyplot as plt

class OscillatoryCircuit:
    def __init__(self, R, L, C):
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
        times = [time for time in range(1000)]
        qs = [self.get_q_by_t(time) for time in times]
        plt.grid(True)
        plt.plot(times, qs)
        plt.show()
