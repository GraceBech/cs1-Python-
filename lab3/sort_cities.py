from lab3.quicksort import *
from lab3.study_cities_driver import cities_list


def compare_population(city1, city2):  # compare the city at one city to the other in size
    return int(city1.population) >= int(city2.population) # if the population for city one is bigger or equal to the population of city 2, return false


def compare_latitude(city1, city2):  # compare the latitudes for the two cities according to their latitudes
    return city1.latitude <= city2.latitude


def compare_name(city1, city2):  # compare the two cities alphabetically
    return city1.name <= city2.name

def sorting(list, func_name):  # sort the two cities
    quick_sort(list, func_name)


sorting(cities_list, compare_population)  # sort the population
fp = open("cities_population.txt", "w")  # open the cities_population file and write  from it
for ele in cities_list:
    fp.write(str(ele) + "\n")  # write from the file
fp.close()  # Close the cities_population file


sorting(cities_list, compare_latitude)
fp1 = open("cities_latitude.txt", "w") # open the latitude file and write from it
for ele in cities_list:
    fp1.write(str(ele) + "\n")
fp1.close()


sorting(cities_list, compare_name)
fp2 = open("cities_alpha.txt", "w")  # open the cities_alpha.txt file and write from it
for ele in cities_list:
    fp2.write(str(ele) + "\n")

fp2.close()
