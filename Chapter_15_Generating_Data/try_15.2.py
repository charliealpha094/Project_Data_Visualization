#Done by Carlos Amaral (20/07/2020)

#Coloured Cubes

import matplotlib.pyplot as plt 

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Set chart title and label axes
ax.set_title("Cubic Values", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cube of Values", fontsize = 14)

#Set the range for each axis.
ax.axis([0, 5000, 0, 5500**3])

plt.show()