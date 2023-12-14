# Author  : Grace Amer Bech
# Date    : 23rd February 2023
# Purpose : Visualize cities (Lab 003)

from cs1lib import *
from lab3.city import City

CENTER_X = 360
CENTER_Y = 180
WIDTH = 720
HEIGHT = 360
RAD = 5
img = load_image("world.png")
cities_list = []
FR = 60
frames = 0
cities_number = 1
MAX_CITIES = 50


def draw():
    global frames, cities_number
    if frames == 50:
        if cities_number <= MAX_CITIES:  # If the number of cities drawn is less than the max number of cities we want
            cities_number += 1  # Keep incrementing the number of cities to draw by one
        frames = 0
    for city in range(0, MAX_CITIES):  # for a city in the range 0 to the last index (50)
        cities_list[city].draw(CENTER_X, CENTER_Y)  # draw the city at index one, with center x and center y
    frames += 1  # Keep incrementing the number of frames as a long as the cities drawn are less than 50



# new_populous = [] # create a list to put the most populous cities in
# def clist():
#     fp = open("cities_population.txt", "r")  # open the cities_population file and read from it
#     for i in fp:  # for i in that file
#         s = i.strip()  # strip that file and set it to a variable s
#         cities = s.split(",")  # remove the extra spaces in the cities
#         city = City(code=None, name=cities[0], region=None, population=cities[1], latitude=cities[2], longitude=cities[3])
#         new_populous.append(city)  # append the city to the empty cities list
#
#     fp.close()  # close the cities_population file
#     return new_populous


def main():
    draw_image(img, 0, 0)
    draw()  # draw the city


# clist()
start_graphics(main, width=WIDTH, height=HEIGHT, framerate=FR)
