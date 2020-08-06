#Done by Carlos Amaral (24/07/2020)


#Try 16.4 - Automatic Indexes.

"""
In this section, we hardcoded the indexes correspond-
ing to the TMIN and TMAX columns. Use the header row to determine the indexes
for these values, so your program can work for Sitka or Death Valley. Use the
station name to automatically generate an appropriate title for your graph
as well.
"""

import csv

from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
place_name = ''

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    max_temp_index = header_row.index('TMAX')
    min_temp_index = header_row.index('TMIN')


    #Get dates, highs and lows.
    dates, highs, lows = [], [], []
    for row in reader:
        place_name = row[name_index]
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format the plot.
title = f"Daily high and low temperatures - 2018 {place_name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
