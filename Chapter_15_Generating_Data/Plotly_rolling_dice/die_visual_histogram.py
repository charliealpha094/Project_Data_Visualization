#Done by Carlos Amaral (21/07/2020)


from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die 

#Create a D6
die = Die()

#Make some rolls and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyse the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, die.num_sides+1))  #Store a bar for each of possible results. Starts at 1 and ends at 6 (6-sided Die)
data = [Bar(x=x_values, y=frequencies)] #Bar()-data set that'll be formatted as bar chart. Needs list of x and y values.

x_axis_config = {'title': 'Result'} #Setting the title of x_axis
y_axis_config = {'title': 'Frequency of Result'}   
my_layout = Layout(title='Results of rolling one D6 1000 times', #Layout() returns object that specifies layout and configuration of the
           xaxis = x_axis_config, yaxis = y_axis_config) #graph as a whole.

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') 
