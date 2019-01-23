import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')
#JDP defining two random arrays of numbers to use as a scatter plot. Here the 
#JDP x numbers are evenly spaced but the y are a bit messier.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0.7, 2.3, 3.6, 3.9, 4.3, 6.2, 7.4, 8.1, 8.9 ])

#JDP plotting the scatter graph - everything should be familiar, or easy to work out!
fig = plt.figure()
plt.scatter(x, y)
plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel("x")
plt.ylabel("y")
plt.grid("on")
plt.title("A Simple Scatter Plot")
plt.savefig("scatter_plot.png")