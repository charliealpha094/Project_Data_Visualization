#Done by Carlos Amaral (18/07/2020)

import matplotlib.pyplot as plt  #1st, import pyplot module, using alias plt, so we don't need to type pyplot repeateadly.

squares = [1, 4, 9, 16, 25]

fig, ax  = plt.subplots()  #Subplots() generates one or more plots in the same figure. Fig, represents the entire figure or collection of plots generated.
ax.plot(squares)  #Variable ax, represents a single plot in the figure.

plt.show()