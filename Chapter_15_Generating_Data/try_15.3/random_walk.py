#Done by Carlos Amaral (20/07/2020)

#Creating the randomWalk() class and Choosing Directions

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):      #Set the default number of points in a walk to 5000.
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks start at (0,0).
        self.x_values = [0]   #Make two lists to hold x and y values, and start each walk at (0,0)
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        #Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:   #Set up a loop that runs until the walk is set up with the correct number of points.

            #Decide which direction to go and how to go in that direction.
            x_direction = choice([1, -1])  #Choose a value for x_direction which returns either 1 for right movement or -1 for left.
            x_distance = choice([0, 1, 2, 3, 4])  
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)