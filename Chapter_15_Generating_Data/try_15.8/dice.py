#Done by Carlos Amaral (22/07/2020)


#Try 15.8 - Multiplication

"""
When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if
you multiply these numbers instead.
"""

from random import randint

class Die():
    """A class representing a single Die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint (1, self.num_sides)
