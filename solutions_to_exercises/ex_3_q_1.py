import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
plt.close('all')

pi = 3.14159
x = np.linspace(-2*pi, 2*pi, 200)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

fig = plt.figure()
#JDP we have to define the figure size here or the aspect ratio of the subplots
#JDP will get messed up - one of the quirks of using gridspec for non-square plots.
fig.set_size_inches(9,3)

grid = gs.GridSpec(nrows=1,ncols=3)

#JDP plotting these, I can use the set_xticks and set_xticklabels functions to 
#JDP define custom x ticks - here in units of pi. I use the same LaTeX greek letter
#JDP formatting to get it to print the answer as a greek letter.
ax1 = plt.subplot(grid[0,0])
plt.plot(x, y)
plt.xlabel('Angle [rad]')
plt.ylabel('Trig(Angle)')
plt.ylim(-1.1,1.1)
plt.xlim(-2*pi,2*pi)
ax1.set_xticks([-2*pi, -pi, 0, pi, 2*pi])
ax1.set_xticklabels(['$-2\pi$','$-\pi$', '0', '$\pi$', '$2\pi$'])
ax1.set_title('Sine of x')

ax2 = plt.subplot(grid[0,1])
plt.plot(x, y2)
plt.xlabel('Angle [rad]')
plt.ylim(-1.1,1.1)
plt.xlim(-2*pi,2*pi)
ax2.set_xticks([-2*pi, -pi, 0, pi, 2*pi])
ax2.set_xticklabels(['$-2\pi$','$-\pi$', '0', '$\pi$', '$2\pi$'])
ax2.set_yticklabels([])
ax2.set_title('Cosine of x')


ax3 = plt.subplot(grid[0,2])
plt.plot(x, y3)
plt.xlabel('Angle [rad]')
plt.ylim(-1.1,1.1)
plt.xlim(-2*pi,2*pi)
ax3.set_xticks([-2*pi, -pi, 0, pi, 2*pi])
ax3.set_xticklabels(['$-2\pi$','$-\pi$', '0', '$\pi$', '$2\pi$'])
ax3.set_yticklabels([])
ax3.set_title('Tangent of x')

#JDP The argument bbox_inches="tight" is necessary for gridspec - as without it
#JDP the axis labels will be clipped off the final figure. It's because strictly
#JDP the axis labels are outside the grid boxes, so you have to force the computer
#JDP to make space for them, which is what this command does. Remove it and see
#JDP what happens to the output file!
plt.savefig('ex_3_q_1.png',bbox_inches="tight")