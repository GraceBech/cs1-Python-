# Author   : Grace Amer Bech
# Date     : 7th March 2023
# Purpose  : Draw the background of the map


from lab4.breath_fast_search import *
from lab4.vertex import Vertex
from lab4.load_graph import *

from cs1lib import *

clicked = False
mouse_x = 0
mouse_y = 0
mouse_x_pressed = 0
mouse_y_pressed = 0


start_vertex = None
goal_vertex = None


def mouse_press(mx, my):
    global mouse_x_pressed, mouse_y_pressed, clicked
    clicked = True    # If the mouse has been pressed, then clicked changes to True
    mouse_x_pressed = mx
    mouse_y_pressed = my

def mouse_move(mx, my):  # detects when the mouse moves
    global mouse_y, mouse_x
    mouse_x = mx
    mouse_y = my


def mouse_release(mx, my):
    global clicked
    clicked = False  # If the mouse has been released then the clicked is False


img = load_image("dartmouth_map.png")
ver_dict = load_graph("dartmouth_graph.txt")


def main():
    global start_vertex, goal_vertex
    clear()
    set_stroke_width(2)  # Draw the lines with a thickness of 2
    draw_image(img, 0, 0)

    for point in ver_dict:

        ver_dict[point].draw_vertices(0, 0, 1)  # draw the point in the dictionary in blue
        ver_dict[point].draw_all_edges(0, 0, 1)  # Draw all the edges at that point and draw them in blue
    for ch in ver_dict:
        if ver_dict[ch].draw_mouse_adjacents(mouse_x_pressed, mouse_y_pressed):  # call mouse_adjacents on that dictionary character
            start_vertex = ver_dict[ch]  # set the start vertex to that dictionary character
            start_vertex.draw_vertices(1, 0, 0)  # draw the starting vertex in red

        elif ver_dict[ch].draw_mouse_adjacents(mouse_x, mouse_y) and clicked:
            goal_vertex = ver_dict[ch]  # set the goal vertex to the character in the vertex
            goal_vertex.draw_vertices(1, 0, 0)  # draw the goal in red

        else:
            ver_dict[ch].draw_vertices(0, 0, 1)  # if all the above conditions are not met, then call draw-vertices on the character, and draw in blue

    path = bfs(start_vertex, goal_vertex)  # set path to be whatever breath fast search sets as the start vertex and the goal


    for direction in range(len(path)-1): # get any points nearby
        path[direction].draw_vertices(1, 0, 0)  # call the draw_vertices on the path, and draw which ever path you take
        path[direction].draw_edges(path[direction+1], 1, 0, 0)  # keep drawing the edges in that path, while incrementing


start_graphics( main, width=1012, height=811, mouse_press=mouse_press, mouse_move=mouse_move)