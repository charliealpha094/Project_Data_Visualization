#Done by Carlos Amaral (22/07/2020)


#Try 15.8 - Multiplication

"""When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if
you multiply these numbers instead.
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Die

#Create two D6 Dices.
die_1 = Die()
die_2 = Die()

#Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#Analyse the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frquency of Result'}
my_layout = Layout(title='Multiplication of rolling two D6 dice 1000 times',
         xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6_d6_mult.html')