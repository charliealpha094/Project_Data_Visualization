#Done by Carlos Amaral (25/07/2020)


#Extracting magnitudes

import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


#Making a list of all earthquackes.
all_eq_dicts = all_eq_data['features']

mags = []   #Empty list to store the magnitudes.
for eq_dict in all_eq_dicts:    #Inside the loop each earthquake is represented by eq_dict.
    mag = eq_dict['properties']['mag'] #Each earthquake's magnitude is stored in 'properties' section of the dictionary under 'mag' key
    mags.append(mag) #Store each magnitude in variable mag, and then append to the lists mags.


print(mags[:10]) #print 1st 10 magnitudes.
