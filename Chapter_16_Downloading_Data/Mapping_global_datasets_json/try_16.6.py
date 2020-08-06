#Done by Carlos Amaral (27/07/2020)


#Try 16.6 - Refactoring

"""
The loop that pulls data from all_eq_dicts uses variables for
the magnitude, longitude, latitude, and title of each earthquake before append-
ing these values to their appropriate lists. This approach was chosen for clar-
ity in how to pull data from a JSON file, but it’s not necessary in your code.
Instead of using these temporary variables, pull each value from eq_dict and
append it to the appropriate list in one line. Doing so should shorten the body
of this loop to just four lines.
"""

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


#Make a list of all earthquakes.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], [] #List called hover_texts, to store the label we'll use for each marker.
for eq_dict in all_eq_dicts:
    mag = mags.append(eq_dict['properties']['mag'])
    lon = lons.append(eq_dict['geometry']['coordinates'][0])
    lat = lats.append(eq_dict['geometry']['coordinates'][1])
    title = hover_texts.append(eq_dict['properties']['title'])  #Pull earthquake info and assign it to the variable title. 
    

print(mags[:10])
print(lons[:5])
print(lats[:5])


#Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,  #Plotly pulls an individual label for each marker it generates.
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },

}]
my_layout = Layout(title='Global earthquakes') 

fig = {'data': data, 'layout': my_layout} 
offline.plot(fig, filename='global_earthquakes.html')  