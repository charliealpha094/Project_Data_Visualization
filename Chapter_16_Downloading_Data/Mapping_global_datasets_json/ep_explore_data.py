#Done by Carlos Amaral (25/07/2020)


import json

#Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #1st, we import json module to load data from file and then store it in all_eq_data.

readable_file = 'data/readable_eq_data.json'  #Create a file to write the same data into a more readable format.
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) #json.dump() function takes a JSON data object and a file object and writes the data 
                                          #to that file.


#Making a list of all earthquakes
all_eq_dicts = all_eq_data['features']  #Take data with key 'features' and store it in all_eq_dicts
print(len(all_eq_dicts)) #




