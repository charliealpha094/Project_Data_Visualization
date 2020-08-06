#Done by Carlos Amaral (21/07/2020)


#Creating the die class

from die import Die

#Create a D6
die = Die()

#Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):  #We set 1000 rolls.
    result = die.roll()
    results.append(result)

# Analyse the results.
frequencies = []
for value in range(1, die.num_sides+1): #loop through the possible values (1 through 6)
    frequency = results.count(value)  #count how many times each number appears in results.
    frequencies.append(frequency) #append how many times each number appears in results to the frequencies list.

print(frequencies)