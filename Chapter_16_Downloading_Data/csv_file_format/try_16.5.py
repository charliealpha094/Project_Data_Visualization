#Done by Carlos Amaral (25/07/2020)


#Try 16.5 - Explore.

"""
Generate a few more visualizations that examine any other
weather aspect you’re interested in for any locations you’re curious about.
"""

#I will analyse the precipitation levels in Portugal in the period July, 2019-
#-July, 2020.

import csv

from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/Portugal_weather_2019_2020.csv'

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)

    #Get dates, highs and lows from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = int(row[9])
            low = int(row[10])
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
title = "Daily high and low temperatures - Portugal July 2019 - July 2020"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)


plt.show()