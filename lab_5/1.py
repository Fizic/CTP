import math

from matplotlib import pyplot as plt


class SpringPendulum:
    def __init__(self, m, g, k):
        self.m = m
        self.g = g
        self.k = k
        self.omega = self.get_omega()

    def get_omega(self):
        return math.sqrt(self.g / self.k)

    def get_x_by_t(self, t: float) -> float:
        return self.m * self.g / self.k * (1 - math.cos(self.omega * t))

    def plot_x_versus_time(self) -> None:
        times = [time / 100 for time in range(2800)]
        values = [self.get_x_by_t(time) for time in times]
        plt.grid(True)
        plt.plot(times, values)
        plt.show()


spring_pendulum = SpringPendulum(0.5, 9.8, 8)
spring_pendulum.plot_x_versus_time()