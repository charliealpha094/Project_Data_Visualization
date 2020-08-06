#Done by Carlos Amaral (21/08/2020)

#Try 15.6 - Two D8's

"""
Create a simulation showing what happens when you roll two
eight-sided dice 1000 times. Try to picture what you think the visualization will
look like before you run the simulation; then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of your
system’s capabilities.
"""

from random import randint

class Die():
    """A class representing a single Die."""

    def __init__(self, num_sides=6):
        """Asssume a six-sided Die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)