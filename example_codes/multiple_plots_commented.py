import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#JDP I have to import the gridspec module now!
import matplotlib.gridspec as gs
plt.close('all')

pi = 3.14159
x = np.linspace(0, 2*pi, 50)
y = np.sin(x)

fig = plt.figure()

#JDP I now define my 2x2 grid, with specific width and height spacings.
grid = gs.GridSpec(nrows=2,ncols=2, wspace=0.1, hspace=0.35)

#JDP plt.subplot adds a plot to a specific element of the grid I just defined,
#JDP here it's element [0,0].
ax1 = plt.subplot(grid[0,0])
#JDP once I create the subplot, the rest is more or less the same as before!
plt.plot(x, y)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(Angle)')
#JDP the plt.text(x,y,'(a)') command adds the text '(a)' at the location defined by x,y 
plt.text(-0.1,0.8,'(a)')

#JDP now I am adding a subplot to a different element - [0,1]
ax2 = plt.subplot(grid[0,1])
plt.plot(x, -y)
plt.xlabel('Angle [rad]')
plt.ylabel('-sin(Angle)')
#JDP these two commands below act on the axes ax2 (not quite the same thing as
#JDP the overall plot plt) - and they set the ticks and tick labels to be on the
#JDP right hand side, so they don't overlap onto the other subplot
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
plt.text(-0.1,0.8,'(b)')

#JDP I now add a third subplot, but spanning two elements in the grid.
ax3 = plt.subplot(grid[1,:])
plt.plot(x, 2*y, label='2sin(x)', color='blue')
#JDP this tick_params command changes the colour of the y axis ticks and labels
#JDP to blue - to match the colour of the plotted function above.
ax3.tick_params(axis='y',color='blue', labelcolor='blue')
ax3.set_ylabel('2sin(Angle)', color='blue')
plt.xlabel('Angle [rad]')
#JDP this is a bit tricky. twinx() is a function that creates a new set of axes (ax4)
#JDP that share the x axis with ax3, but have a different y axis.
ax4 = ax3.twinx()
plt.plot(x, -2*y, label='-2sin(x)', color='red')
plt.xlabel('Angle [rad]')
#JDP now we change the colour of the new y axis to red, to match the plotted function
ax4.set_ylabel('-2sin(Angle)', color='red')
ax4.tick_params(axis='y',color='red', labelcolor='red')
#JDP finally, this but just changes the colour of the edges of the box surrounding
#JDP this subplot, so they also match the plotted functions
ax4.spines['right'].set_color('red')
ax4.spines['left'].set_color('blue')
plt.text(-0.2,1.6,'(c)')

fig.suptitle("An Example of Multiple Plots")
plt.savefig('multiple_plots.png')