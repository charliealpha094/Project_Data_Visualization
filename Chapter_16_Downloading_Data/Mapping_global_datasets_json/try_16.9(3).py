#Done by Carlos Amaral (29/07/2020)


#Try 16.9 - World Fires

"""
In the resources for this chapter, you’ll find a file called
world_fires_1_day.csv. This file contains information about fires burning in dif-
ferent locations around the globe, including the latitude and longitude, and the
brightness of each fire. Using the data processing work from the first part of
this chapter and the mapping work from this section, make a map that shows
which parts of the world are affected by fires.
You can download more recent versions of this data at https://earthdata
.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You
can find links to the data in CSV format in the TXT section.
"""

#This file countains information about the fires in europe during last 7 days.
#Date:28/07/2020


import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from datetime import datetime


filename = 'data/MODIS_C6_Europe_7d.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get brightnesses, lats and lons, and dates.
    dates, brightnesses = [], []
    latitudes, longitudes = [], []
    hover_texts = []

    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        latitudes.append(row[0])
        longitudes.append(row[1])
        hover_texts.append(label)
        
       

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='European recent Fire activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='euro_recent_fires.html')
