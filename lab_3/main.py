from math import cos, sin, sqrt, radians

import matplotlib.pyplot as plt


class Projectile:
    def __init__(self, v0: int, height: int):
        self.v0 = v0
        self.height = height

    def get_coordinates(self, angle: float):
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
        return coords_x, coords_y

    def create_schedule(self, angle: float):
        """
        Method for creating schedule of the projectile
        :param angle: Shot Angle
        :return:
        """
        # Create lists for coordinates in different time

        coords_x, coords_y = self.get_coordinates(angle)
        plt.plot(coords_x, coords_y)
        plt.show()

    def create_multi_schedule(self):
        all_coords = []
        for i in range(0, 90, 10):
            coords_x, coords_y = self.get_coordinates(radians(i))
            all_coords.append(coords_x)
            all_coords.append(coords_y)
        plt.plot(*all_coords)
        plt.show()

    def get_distance(self, angle: float):
        """
        Method for calculating the distance of the projectile
        :param angle: Shot Angle
        :return: distance
        """
        time = (self.v0 * sin(angle) + sqrt(self.v0 ** 2 * sin(angle) ** 2 + 2 * 10 * self.height)) / 10
        return self.v0 * cos(angle) * time

    def create_schedule_distance_versus_angle(self):
        """
        Method for creating schedule of the distance versus angle
        :return:
        """
        angles = [angle for angle in range(0, 90)]
        distances = [self.get_distance(radians(angle)) for angle in angles]
        plt.plot(angles, distances)
        plt.show()

    def create_schedule_distance_versus_v0(self):
        angles = [angle for angle in range(0, 90)]
        distances = [self.get_distance(radians(angle)) for angle in angles]
        plt.plot(distances, angles)
        plt.show()


projectile = Projectile(200, 70)
projectile.create_schedule(radians(58))
projectile.create_multi_schedule()
max_d, angle_d = 0, 0
for angle in range(0, 90):
    if projectile.get_distance(radians(angle)) > max_d:
        max_d = projectile.get_distance(radians(angle))
        angle_d = angle

print(f'Max distance: {max_d}, angle: {angle_d}')
projectile.create_schedule_distance_versus_angle()
shooter = Projectile(300, 0)
shooter.create_schedule_distance_versus_v0()