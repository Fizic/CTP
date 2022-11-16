import matplotlib
import math

class Pendulum:
    def __init__(self, amplitude_x, amplitude_y, length, mass, gravity):
        self.amplitude_x = amplitude_x
        self.amplitude_y = amplitude_y
        self.length = length
        self.mass = mass
        self.gravity = gravity

        self.period = self.get_period()

        def get_period(self):
            return 2 * math.pi * math.sqrt(self.length / self.gravity)
