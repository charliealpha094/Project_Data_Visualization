#Done by Carlos Amaral (26/07/2020)


#Building a world map

import json

from plotly.graph_objs import Scattergeo, Layout #Import the Scattergeo chart type and the Layout class.
from plotly import offline #Import the offline module to render the map.

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


#Make a list of all earthquakes.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict  in all_eq_dicts:
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
data = [Scattergeo(lon=lons, lat=lats)]  #Define a list called data and create Scattergeo module inside the list.
my_layout = Layout(title='Global earthquakes') #Give chart a title.

fig = {'data': data, 'layout': my_layout} #Create dictionary called fig that contains data and layout.
offline.plot(fig, filename='global_earthquakes.html')  #Plot() function with a descriptive name for the output.
