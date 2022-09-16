from math import cos, sin, pi
import matplotlib.pyplot as plt


class Planet:
    """
    Class for describing planets
    """
    def __init__(self, name, radius, day_in_year):
        self.name = name
        self.radius = radius
        self.day_in_year = day_in_year

    def get_coords_from_time_x(self, time: int) -> float:
        """
        Method for calculating x coordinate of the planet on a specific day
        :param time: time in days
        :return: x coordinate of the planet on a specific day
        """
        return self.radius * cos(2 * pi * time / self.day_in_year)

    def get_coords_from_time_y(self, time: int) -> float:
        """
        Method for calculating y coordinate of the planet on a specific day
        :param time: time in days
        :return: y coordinate of the planet on a specific day
        """
        return self.radius * sin(2 * pi * time / self.day_in_year)

    def create_schedule(self, second_planet, time: int):
        """
        Method for creating schedule of the planets
        :param second_planet: planet for which it is necessary to calculate the trajectory
        :param time: time in days
        :return:
        """
        # Create lists for coordinates in different time
        coords_x = []
        coords_y = []
        # We fill in the coordinates for every 11 days
        for i in range(11, time, 11):
            coords_x.append(second_planet.get_coords_from_time_x(i) - self.get_coords_from_time_x(i))
            coords_y.append(second_planet.get_coords_from_time_y(i) - self.get_coords_from_time_y(i))
        plt.plot(coords_x, coords_y)
        plt.show()

    def __str__(self):
        return f'Planet {self.name} with radius {self.radius} day in year {self.day_in_year}'


# Creating planets
mars = Planet('Mars', 1.52, 687)
earth = Planet('Earth', 1, 365)
saturn = Planet('Saturn', 9.58, 10759)
venir = Planet('Venir', 0.72, 225)
jupiter = Planet('Jupiter', 5.20, 4332)

# Creating schedule of the planets, where the first planet is the center of the coordinate system
# and the second planet is the planet for which it is necessary to calculate the trajectory
# The third parameter is the time in days, selected by experience
earth.create_schedule(mars, 12000)
earth.create_schedule(saturn, 23000)
earth.create_schedule(venir, 40000)
venir.create_schedule(jupiter, 32000)
