#Done by Carlos Amaral (22/07/2020)


#Try 15.9 - Die Comprehensions

"""
For clarity, the listings in this section use the long
form of for loops. If you’re comfortable using list comprehensions, try writing a
comprehension for one or both of the loops in each of these programs.
"""

from random import randint

class Die():
    """A class representing a single Die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)