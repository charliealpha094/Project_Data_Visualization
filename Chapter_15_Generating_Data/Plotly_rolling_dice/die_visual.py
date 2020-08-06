#Done by Carlos Amaral (21/07/2020)


#Creating the Die Class

from die import Die

#Create a D6.
die = Die()

#Make some rolls, and store results in a list.
results = []

for roll_num in range(100):  #We roll the die 100 times.
    result = die.roll()
    results.append(result)

print(results)
