# Author   : Grace Amer Bech
# Date     : 23 rd February 2023
# Purpose  : Lab 3

from cs1lib import *
from random import uniform


class City:
    def __init__(self, code, name, region, population, latitude, longitude):
        self.code = str(code)
        self.name = str(name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.r = uniform(0, 1)
        self.g = uniform(0, 1)
        self.b = uniform(0, 1)

    def __str__(self):
        return (self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(
            self.longitude))  # return the values as a string separated by commas

    def draw(self, cx, cy):
        set_fill_color(self.r, self.g, self.b)  # draw the city in orange
        lat = self.latitude * 2
        long = self.longitude * 2
        px = cx + long
        py = cy - lat

        # py = cy - (360 / 2 - (self.latitude * 2))  # one latitude is half the pixels
        # px = cx + (720 / 2 + (self.longitude * 2))  # one longitude is half the pixel, hence multiply by two
        RAD = 5
        draw_circle(px, py, RAD)  # draw the circle representing the city

# fp = open("world_cities.txt", "r")
