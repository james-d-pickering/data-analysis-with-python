import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#JDP closing all open plots before we start
plt.close('all')

#JDP defining our variables - all should be familiar. We use the function np.exp()
#JDP to help us produce a Gaussian distribution - can you see how?
pi = 3.14159
x = np.linspace(-2*pi, 2*pi, 500)
y1 = np.exp(-(x)**2/6)
y2 = y1*np.sin(2*x)
y3 = -y1
y4 = y3*np.sin(2*x)

#JDP here we're defining some similar things to above, but with less data points
#JDP (50 vs 500) - this means when we plot a scatter plot we can see it! 500 points
#JDP on a scatter plot would just look like a mess.
x_scatter = np.linspace(-2*pi, 2*pi, 50)
y1_scatter = np.exp(-(x_scatter)**2/6)
y2_scatter = -y1_scatter

fig = plt.figure()

#JDP Using many different plot commands as we're plotting several things on top of
#JDP one another.
plt.plot( x, y1, color='black', label='Envelope 1' )
plt.plot( x, y2, color='blue', linestyle='--', label='Carrier 1' )
plt.plot( x, y3, color='red', label='Envelope 2' )
plt.plot( x, y4, color='green', linestyle=':', label='Carrier 2' )
#JDP the plt.fill() command shades in the area between the plot and the x axis 
#JDP - a bit like how an integral would
plt.fill(x, y1, color='orange', alpha=0.3)
plt.fill(x, -y1, color='purple', alpha=0.3)
plt.scatter(x_scatter, y1_scatter, marker='x', alpha=0.6, color ='black' )
plt.scatter(x_scatter, y2_scatter, marker='o', alpha=0.6, color='red' )
#JDP this plt.legend() function adds the legend, and sets the location with the 
#JDP loc argument, try different numbers and see the effect.
plt.legend(loc=4)

#JDP this command plt.gca is short for Get Current Axes - and just helps us later on
ax = plt.gca()

plt.xlim(-2*pi,2*pi)
#JDP the following two lines set the ticks for the major and minor axes. Notice that
#JDP i have to use ax.set_xticks to set the minor ticks, and thats why I had to use
#JDP plt.gca earlier to get hold of the axes.
plt.xticks(np.linspace(-2*pi, 2*pi, 5), ["$-2\pi$", "$-\pi$", 0, "$\pi$", "$2\pi$"])
ax.set_xticks(np.linspace(-2*pi, 2*pi, 17), minor=True)
plt.xlabel("Phase [rad]", family='serif')

#JDP this is as above but for the y axes
plt.ylim(-1.25,1.25)
plt.yticks(np.linspace(-1,1,5))
ax.set_yticks(np.linspace(-1,1,9), minor=True)
plt.ylabel("Intensity [arb. units.]", family='serif')

#JDP adding titles and grid lines - I've changed the font family to serif
plt.title("A Fancy Plot", family='serif', size='xx-large')
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

plt.savefig("fancy_plot.png")