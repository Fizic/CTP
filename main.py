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

    def __str__(self):
        return f'Planet {self.name} with radius {self.radius} and mass {self.mass} and day in year {self.day_in_year}'


def create_schedule(first_planet, second_planet, time):
    coords_x = []
    coords_y = []
    for i in range(11, time, 11):
        coords_x.append(first_planet.get_coords_from_time_x(i) - second_planet.get_coords_from_time_x(i))
        coords_y.append(first_planet.get_coords_from_time_y(i) - second_planet.get_coords_from_time_y(i))
    plt.plot(coords_x, coords_y)
    plt.show()


mars = Planet('Mars', 1.52, 687)
earth = Planet('Earth', 1, 365)
saturn = Planet('Saturn', 9.58, 10759)
venir = Planet('Venir', 0.72, 225)
jupiter = Planet('Jupiter', 5.20, 4332)

create_schedule(mars, earth, 12000)
create_schedule(saturn, earth, 40000)
create_schedule(venir, earth, 20000)
create_schedule(earth, jupiter, 40000)
