# Author    : Grace Amer Bech
# Date      : March 9th 2023
# Purpose   : Breath Fast search



from collections import deque


def bfs(start_vertex, goal_vertex):  # def breath first search and pass in the start vertex and the goal vertex

    frontier = deque()
    back_pointer_dict = {}

    frontier.append(start_vertex)
    back_pointer_dict[start_vertex] = None

    while len(frontier) != 0 and goal_vertex not in back_pointer_dict:
        current_vertex = frontier.popleft()

        for vertex in current_vertex.adjacentlist:
            if vertex not in back_pointer_dict:
                frontier.append(vertex)
                back_pointer_dict[vertex] = current_vertex

    goal = goal_vertex
    path = []

    while goal != None:  # if the goal vertex is not None, then, append that goal to path
        path.append(goal)
        back = back_pointer_dict[goal]  # set the back_pointer to be the value of the goal
        goal = back  # equate goal_vertex to the back_pointer

    path.append(start_vertex)  # add the start vertex to the path

    return path



