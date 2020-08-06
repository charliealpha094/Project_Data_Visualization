#Done by Carlos Amaral (28/07/2020)


import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/significant_month.geojson.json'
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
    

print(mags)
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