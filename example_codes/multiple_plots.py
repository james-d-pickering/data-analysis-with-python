import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
plt.close('all')

pi = 3.14159
x = np.linspace(0, 2*pi, 50)
y = np.sin(x)

fig = plt.figure()

grid = gs.GridSpec(nrows=2,ncols=2, wspace=0.1, hspace=0.35)

ax1 = plt.subplot(grid[0,0])
plt.plot(x, y)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(Angle)')
plt.text(-0.1,0.8,'(a)')

ax2 = plt.subplot(grid[0,1])
plt.plot(x, -y)
plt.xlabel('Angle [rad]')
plt.ylabel('-sin(Angle)')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
plt.text(-0.1,0.8,'(b)')

ax3 = plt.subplot(grid[1,:])
plt.plot(x, 2*y, label='2sin(x)', color='blue')
ax3.tick_params(axis='y',color='blue', labelcolor='blue')
ax3.set_ylabel('2sin(Angle)', color='blue')
plt.xlabel('Angle [rad]')
ax4 = ax3.twinx()
plt.plot(x, -2*y, label='-2sin(x)', color='red')
plt.xlabel('Angle [rad]')
ax4.set_ylabel('-2sin(Angle)', color='red')
ax4.tick_params(axis='y',color='red', labelcolor='red')
ax4.spines['right'].set_color('red')
ax4.spines['left'].set_color('blue')
plt.text(-0.2,1.6,'(c)')

fig.suptitle("An Example of Multiple Plots")
plt.savefig('multiple_plots.png')