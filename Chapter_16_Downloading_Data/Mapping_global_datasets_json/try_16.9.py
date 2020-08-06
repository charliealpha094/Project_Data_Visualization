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
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/MODIS_C6_Europe_7d.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    #Get latitude, longitude and brightness from this file.
    latitudes, longitudes, brightnesses, dates = [], [], [], []
    hover_texts = []
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        latitude = float(row[0])
        longitude = float(row[1])
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"
        dates.append(date)
        latitudes.append(latitude)
        longitudes.append(longitude)
        hover_texts.append(label)


#Map the fires
data = [{
    'type': 'scattergeo',
    'latitude': latitudes,
    'longitude': longitudes,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightness,
        'colorscale': 'YlGnBu',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},

    },
    
}]
my_layout = Layout(title="Recent european fire activity.")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='euro_fires.html')

    

