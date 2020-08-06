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

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        #Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            #Decide in which direction to go and how to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()   

            #Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Determine the direction and distance for each step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = direction * distance
        return step

