#Done by Carlos Amaral (25/07/2020)


#Extracting Location Data

import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readible_file = 'data/readable_eq_data.json'
with open(readible_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


#Make a list of all earthquakes.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])