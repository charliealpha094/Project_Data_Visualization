#Done by Carlos Amaral (20/07/2020)


#Try 15.1 - Cubes

import matplotlib.pyplot as plt 

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

#Set chart title and labels
ax.set_title("Cubic Values", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cube of values", fontsize = 14)

plt.show()