#Done by Carlos Amaral (23/07/2020)


#Try 16.2 - Sitka-Death Valley Comparision

"""
The temperature scales on the Sitka and
Death Valley graphs reflect the different data ranges. To accurately compare
the temperature range in Sitka to that of Death Valley, you need identical
scales on the y-axis. Change the settings for the y-axis on one or both of the
charts in Figures 16-5 and 16-6. Then make a direct comparison between
temperature ranges in Sitka and Death Valley (or any two places you want to
compare).
"""

#ylim for sitka

import csv

from datetime import datetime
import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get dates, and high and low temperatures from this file.
    dates, highs, lows  = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()   #Draws date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()