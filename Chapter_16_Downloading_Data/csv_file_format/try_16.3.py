#Done by Carlos Amaral (24/07/2020)


#Try 16.3- San Francisco

"""
Are temperatures in San Francisco more like tempera-
tures in Sitka or temperatures in Death Valley? Download some data for San
Francisco, and generate a high-low temperature plot for San Francisco to
make a comparison.
"""

import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_francisco_weather_2019-2020.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    #Get dates, and maximum and minimum temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
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
title = "Daily high and low temperatures - San Francisco 2019 - 2020"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()