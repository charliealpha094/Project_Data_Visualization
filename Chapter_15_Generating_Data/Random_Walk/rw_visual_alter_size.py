#Done by Carlos Amaral (20/07/2020)


import matplotlib.pyplot as plt 
from random_walk import RandomWalk 

#Keep making new walks as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break