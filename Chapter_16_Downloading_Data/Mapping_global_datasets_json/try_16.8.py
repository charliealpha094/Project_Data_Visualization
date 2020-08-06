#Done by Carlos Amaral (28/07/2020)


#Try 16.8 - Recent Earthquakes.

"""
You can find data files containing information about
the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods
online. Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
and you’ll see a list of links to data sets for various time periods, focusing on
earthquakes of different magnitudes. Download one of these data sets, and
create a visualization of the most recent earthquake activity.
"""
#Date: 28/07/2020 - Last 30 days significative earthquakes.

import json


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/significant_month.geojson.json'
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']

all_eq_dicts = all_eq_data['features']

dates, mags, lons, lats, hover_texts= [], [], [], [], []
for eq_dict in all_eq_dicts:
    date = dates.append(eq_dict['properties']['time'])
    mag = mags.append(eq_dict['properties']['mag'])
    lon = lons.append(eq_dict['geometry']['coordinates'][0])
    lat = lats.append(eq_dict['geometry']['coordinates'][1])
    title = hover_texts.append(eq_dict['properties']['title'])

print(mags)
print(dates[:5])
print(lons[:5])
print(lats[:5])


#Map the earthquakes
data = [{
    'type:': 'scattergeo',
    'date': dates,
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],

        'color': mags,
        'colorscale': 'Viridis',
        'reverscale': True,
        'colorbar': {'title': 'Magnitude'},
    },

}]
my_layout = Layout(title=title)
offline.plot(fig, filename='global_earthquakes.html')


