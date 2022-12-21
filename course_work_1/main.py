import matplotlib.pyplot as plt
import math


class Pendulum:
    def __init__(self, initial_phase_x: float, initial_phase_y: float, omega_x: float, omega_y: float):
        self.initial_phase_x = initial_phase_x
        self.initial_phase_y = initial_phase_y
        self.omega_x = omega_x
        self.omega_y = omega_y
        self.amplitude_x = 1
        self.amplitude_y = 1

    def get_x_by_t(self, t: float) -> float:
        return self.amplitude_x * math.cos(t * self.omega_x + self.initial_phase_x)

    def get_y_by_t(self, t: float) -> float:
        return self.amplitude_y * math.cos(t * self.omega_y + self.initial_phase_y)

    def plot_x_y_versus_time(self) -> None:
        times = [time / 100 for time in range(30000)]
        values_x = [self.get_x_by_t(time) for time in times]
        values_y = [self.get_y_by_t(time) for time in times]
        f = plt.figure()
        f.set_figwidth(5)
        f.set_figheight(5)
        plt.plot(values_x, values_y)
        plt.show()


if __name__ == '__main__':
    print("Введите начальную фазу по оси X:")
    initial_phase_x = float(input())
    print("Введите начальную фазу по оси Y:")
    initial_phase_y = float(input())
    print("Введите угловую частоту по оси X:")
    omega_x = float(input())
    print("Введите угловую частоту по оси Y:")
    omega_y = float(input())
    pendulum = Pendulum(initial_phase_x, initial_phase_y, omega_x, omega_y)
    pendulum.plot_x_y_versus_time()
