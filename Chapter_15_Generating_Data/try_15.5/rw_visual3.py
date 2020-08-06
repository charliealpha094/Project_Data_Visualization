#Done by Carlos Amaral (20/07/2020)


#try 15.5- Refactoring

"""
The fill_walk() method is lengthy. Create a new method
called get_step() to determine the direction and distance for each step, and
then calculate the step. You should end up with two calls to get_step() in
fill_walk() :
x_step = self.get_step()
y_step = self.get_step()
This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.
"""

import matplotlib.pyplot as plt 

from random_walk3 import RandomWalk

#Keep making new walks as long as the program is active.
while True:
    #Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)

    
    #Emphasize the first and last points
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=15)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

 


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break