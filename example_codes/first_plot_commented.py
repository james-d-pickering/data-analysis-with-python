import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')

#JDP here I define all variables, pi, a linearly spaced list of 50 numbers between
#JDP zero and 2*pi, and also the sine of that list.
pi = 3.14159
x = np.linspace(0, 2*pi, 50)
y = np.sin(x)

#JDP plt.figure creates the blank figure
fig = plt.figure()
#JDP plt.plot adds the x and y data we want to plot
plt.plot(x, y)
#JDP plt.xlim sets the bit of the x axis we want to look at (between 0 and 2pi)
plt.xlim(0, 2*pi)
#JDP these two set the labels for the x and y axes
plt.xlabel('x [rad]')
plt.ylabel('sin(x)')
#JDP this adds a title
plt.title('A Simple Plot')
#JDP this turns on grid lines
plt.grid('on')
#JDP this saves the figure!
plt.savefig('first_plot.png')