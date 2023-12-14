# Author  : Grace Amer Bech
# Date    : 4th March 2023
# Purpose : lab 4 analysing sorting algorithms


from lab4.vertex import Vertex


def load_graph(graph):

    ver_dict = {}   # create an empty vertex dictionary
    fp = open(graph, "r")  # open the graph file and read from it

    for line in fp:  # for every line in the file
        wlist = line.split(";")  # split every line using a semicolon
        vname = wlist[0].strip()  # strip the first index
        v_x = wlist[2].strip().split(',')[0]  # set the x coordinate to the second index and then strip it an split it. X is the first index in its list
        v_y = wlist[2].strip().split(',')[1]  # set the y coordinate to the second index and then strip it an split it. y is the first index in the coordinate list
        v = Vertex(vname, v_x, v_y,[])  # Assign v as a reference to the vertex objects
        ver_dict[vname] = v

    fp.close()

    fp1 = open(graph, "r")

    for l in fp1:  # for every line in the file
        wlist = l.split(";")   # split it using a semicolon
        vname = wlist[0].strip()
        v1 = ver_dict[vname]
        adjacent_name_list = wlist[1].strip().split(",")   # names of adj list in form of list


        for name in adjacent_name_list: # loop over the adjacents name list and get a name
            v1.adjacentlist.append(ver_dict[name.strip()]) # append the name into the list and strip it


#
    fp1.close()
    return ver_dict




