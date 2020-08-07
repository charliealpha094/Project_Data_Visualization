#Done by Carlos Amaral (26/07/2020)


#Customizing Marker Size.

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as  f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
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

#Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {   #'marker' specifies how big each marker on map should be.
        'size': [5*mag for mag in mags],  #list comprehension that generates an appropriate marker size for each value in mags list.
    },
}]
my_layout = Layout(title='Global earthquakes') #Give chart a title.

fig = {'data': data, 'layout': my_layout} 
offline.plot(fig, filename='global_earthquakes.html')  
