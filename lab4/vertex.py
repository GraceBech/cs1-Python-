# Author  : Grace Amer Bech
# Date    : 4th March 2023
# Purpose : lab 4 analysing sorting algorithms

from cs1lib import *

class Vertex:
    def __init__(self, name, vertex_x, vertex_y, adjacent_list):
        self.name = name
        self.vertex_x = int(vertex_x)  # change the x coordinate into an integer
        self.vertex_y = int(vertex_y)   # change the x coordinate into an integer
        self.adjacentlist = adjacent_list
        self.radius = 10



    # def link_vertices(self, vertex, r, g, b):
    #     set_fill_color(r, g, b)
    #     set_stroke_color(r, g, b)
    #     draw_line(self.vertex_x, self.vertex_y, vertex.vertex_x, vertex.vertex_y)


    def adjacent_list(self):
        adjacent_list1 = []

        for i in self.adjacentlist: # for every element in the adjacent list, append the name of the adjacents
            adjacent_list1.append(i.name)

        return adjacent_list1


    def __str__(self):  # return everything as a string and use join set the vertices into strings
        return self.name + ';' + " " + "location:" + " " + str(self.vertex_x) + "," + " " + str(self.vertex_y) + ";" + " " + "adjacent vertices:" \
            + " " + ", ".join(self.adjacent_list())

    def draw_edges(self, vertex, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_line(self.vertex_x, self.vertex_y, vertex.vertex_x, vertex.vertex_y)  # draw a line using this points to connect all the edges

    def draw_all_edges(self, r, g, b):
        for element in self.adjacentlist:
            self.draw_edges(element, r, g, b)

    def draw_vertices(self, r, g, b):

        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.vertex_x, self.vertex_y, 4)


    def draw_mouse_adjacents(self, mx, my):
        if self.vertex_x - self.radius <= mx <= self.vertex_x + self.radius and self.vertex_y - self.radius <= my <= self.vertex_y + self.radius:
            return True
        else:
            return False


