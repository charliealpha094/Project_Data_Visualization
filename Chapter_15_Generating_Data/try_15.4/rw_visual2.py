#Done by Carlos Amaral (20/07/2020)


"""15-3. Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with
plt.plot() . To simulate the path of a pollen grain on the surface of a drop of
water, pass in the rw.x_values and rw.y_values , and include a linewidth argu-
ment. Use 5000 instead of 50,000 points."""




#Plotting the random walk

import matplotlib.pyplot as plt 

from random_walk2 import RandomWalk

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