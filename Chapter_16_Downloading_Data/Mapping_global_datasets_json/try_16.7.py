#Done by Carlos Amaral (28/07/2020)


#Try 16.7 - Automated title

"""
In this section, we specified the title manually when defin-
ing my_layout , which means we have to remember to update the title every
time the source file changes. Instead, you can use the title for the data set in
the metadata part of the JSON file. Pull this value, assign it to a variable, and
use this for the title of the map when you’re defining my_layout .
"""

import json

from plotly.graph_ojs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)


title = all_eq_data['metadata']['title']

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = mags.append(eq_dict['properties']['mag'])
    lon = lons.append(eq_dict['geometry']['coordinates'][0])
    lat = lats.append(eq_dict['geometry']['coordinates'][1])
    title = hover_texts.append(eq_dict['properties']['title'])

print(mags[:10])
print(lons[:5])
print(lats[:5])


#Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':  'Magnitude'},
    },
}]

my_layout = Layout(title=title)
offline.plot(fig, filename='global_earthquakes.html')  