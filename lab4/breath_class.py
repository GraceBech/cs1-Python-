# Author    : Grace Amer Bech
# Date      : March 9th 2023
# Purpose   : Breath Fast search

class Breath_search:
    def __init__(self, distance, back_pointer, visited):
        self.distance = distance
        self.back_pointer = back_pointer
        self.visited = visited

        # if self.distance == None:
        #     self.visited == None
        #
        #
        # if self.distance != None:
        #     self.visited == True

