# Author  : Grace Amer Bech
# Date    : 23 rd February 2023
# Purpose : Lab 3 / writing into a file

from lab3.study_cities_driver import *

fp_w = open("City", "w")  # open the file City from the study_cities_driver and write from it
# c = cities_list()

for city in c:  # for any city in the city thing

    fp_w.write(str(city) + "\n")  # write the city and strip it

fp_w.close()  # close the file

