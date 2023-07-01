

# 5. Write a python script to create a dict object from a list of city names in such a way
# the alphabets are keys of the dictionary and list of city names starting from that
# alphabet will be its data value.


city_list = input("Enter city names : (seperated by spaces):").split(" ")
city_dict = {}

available_alfa = ""

for city in city_list:
    if city[0] not in city_dict:
        city_dict[city[0]] = [city]
    else:
        city_dict[city[0]].append(city)

print(city_dict)