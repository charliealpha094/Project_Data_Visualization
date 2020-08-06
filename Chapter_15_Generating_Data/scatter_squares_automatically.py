#Done by Carlos Amaral (19/07/2020)


import matplotlib.pyplot as plt 

x_values = range(1, 1001)     #Start with a range of x-values countaining the numbers  through 1000.
y_values = [x**2 for x in x_values]  #A list comprehension generates y values by looping through x-values, squaring each no. (x**2) 
#and storing the results in y_values

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10) #We pass the input and output lists to scatter()

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the range for each axis.
ax.axis([0, 1100, 0, 1100000]) #We use the axis() method to specify the range of each axis. It requires four values.
#The minimum and maximum values for the x-axis and y-axis.

plt.show()
