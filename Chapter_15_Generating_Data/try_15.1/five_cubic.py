#Done by Carlos Amaral (19/07/2020)


#Try 15.1- Cubes

import matplotlib.pyplot as plt 

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth = 3)

#Set chart title and label axes
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cubic of Values", fontsize = 14)

#Set  size tick labels
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()