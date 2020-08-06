#Done by Carlos Amaral (20/07/2020)


#Plotting the random walk

import matplotlib.pyplot as plt 

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()