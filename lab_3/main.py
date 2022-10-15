from math import cos, sin, sqrt, radians

import matplotlib.pyplot as plt


class Projectile:
    def __init__(self, v0: int, height: int):
        self.v0 = v0
        self.height = height

    def create_schedule(self, angle: float):
        """
        Method for creating schedule of the projectile
        :param angle: Shot Angle
        :return:
        """
        # Create lists for coordinates in different time
        coords_x = []
        coords_y = []
        # We fill in the coordinates for every 1 second
        y_now = self.height
        time = 0
        while y_now >= 0:
            coords_x.append(self.v0 * cos(angle) * time)
            coords_y.append(y_now)
            time += 0.01
            y_now = self.height + self.v0 * sin(angle) * time - 10 * time ** 2 / 2

        plt.plot(coords_x, coords_y)
        plt.show()

    def get_distance(self, angle: float):
        """
        Method for calculating the distance of the projectile
        :param angle: Shot Angle
        :return: distance
        """
        time = (self.v0 * sin(angle) + sqrt(self.v0 ** 2 * sin(angle) ** 2 + 2 * 10 * self.height)) / 10
        return self.v0 * cos(angle) * time


project = Projectile(200, 70)
max_d, angle_d = 0, 0
for i in range(0, 90000):
    if project.get_distance(radians(i / 1000)) > max_d:
        max_d = project.get_distance(radians(i / 1000))
        angle_d = i / 1000

print(f'Max distance: {max_d}, angle: {angle_d}')