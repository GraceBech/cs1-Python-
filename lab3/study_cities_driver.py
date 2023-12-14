from lab3.city import City

cities_list = []


fp = open("world_cities.txt", "r") # open the world cities file and read from it

for i in fp:  # for any city in the file
    s = i.strip()  # strip the city
    cities = s.split(",")
    c = cities
    city = City(c[0], c[1], c[2], c[3], c[4], c[5])  # get the city at the respective indices

    cities_list.append(city)  # append the city to the empy city list

fp.close()  # close the world city file in which you read from


cp = open("city.txt", "w")

for elem in cities_list:
    city = str(elem)
    cp.write(city + "\n")




cp.close()





