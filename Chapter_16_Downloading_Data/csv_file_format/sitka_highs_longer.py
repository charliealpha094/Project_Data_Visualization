#Done by Carlos Amaral (22/07/2020)


#Plotting a Longer Timeframe

import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

      #Get dates and high temperatures from this file.
    dates, highs = [], []   #Create 2 empty lists to store dates and high temperatures from the file.
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') #Convert data containing date info (raw[2]) to a datetime object and append to dates.
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#Format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()   #Draws date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
