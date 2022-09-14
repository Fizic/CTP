from math import cos, sin, pi
import matplotlib.pyplot as plt


class Planet:
    def __init__(self, name, radius, day_in_year):
        self.name = name
        self.radius = radius
        self.day_in_year = day_in_year

    def get_coords_from_time_x(self, time):
        return self.radius * cos(2 * pi * time / self.day_in_year)

    def get_coords_from_time_y(self, time):
        return self.radius * sin(2 * pi * time / self.day_in_year)

    def create_schedule(self, second_planet, time):
        coords_x = []
        coords_y = []
        for i in range(11, time, 11):
            coords_x.append(second_planet.get_coords_from_time_x(i) - self.get_coords_from_time_x(i))
            coords_y.append(second_planet.get_coords_from_time_y(i) - self.get_coords_from_time_y(i))
        plt.plot(coords_x, coords_y)
        plt.show()

    def __str__(self):
        return f'Planet {self.name} with radius {self.radius} day in year {self.day_in_year}'


mars = Planet('Mars', 1.52, 687)
earth = Planet('Earth', 1, 365)
saturn = Planet('Saturn', 9.58, 10759)
venir = Planet('Venir', 0.72, 225)
jupiter = Planet('Jupiter', 5.20, 4332)

earth.create_schedule(mars, 12000)
earth.create_schedule(saturn, 23000)
earth.create_schedule(venir, 40000)
venir.create_schedule(jupiter, 32000)
