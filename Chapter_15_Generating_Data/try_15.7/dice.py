#Done by Carlos Amaral (21/07/2020)

#Try 15.7 - Three Dice

"""
When you roll three D6 dice, the smallest number you can roll
is 3 and the largest number is 18. Create a visualization that shows what hap-
pens when you roll three D6 dice.
"""

from random import randint

class Die():
    """A class representing a single Die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided Die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
        