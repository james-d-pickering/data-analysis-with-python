import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

pi = 3.14159
x = np.linspace(-2*pi, 2*pi, 500)
y1 = np.exp(-(x)**2/6)
y2 = y1*np.sin(2*x)
y3 = -y1
y4 = y3*np.sin(2*x)

x_scatter = np.linspace(-2*pi, 2*pi, 50)
y1_scatter = np.exp(-(x_scatter)**2/6)
y2_scatter = -y1_scatter

fig = plt.figure()

plt.plot( x, y1, color='black', label='Envelope 1' )
plt.plot( x, y2, color='blue', linestyle='--', label='Carrier 1' )
plt.plot( x, y3, color='red', label='Envelope 2' )
plt.plot( x, y4, color='green', linestyle=':', label='Carrier 2' )
plt.fill(x, y1, color='orange', alpha=0.3)
plt.fill(x, -y1, color='purple', alpha=0.3)
plt.scatter(x_scatter, y1_scatter, marker='x', alpha=0.6, color ='black' )
plt.scatter(x_scatter, y2_scatter, marker='o', alpha=0.6, color='red' )
plt.legend(loc=4)
ax = plt.gca()

plt.xlim(-2*pi,2*pi)
plt.xticks(np.linspace(-2*pi, 2*pi, 5), ["$-2\pi$", "$-\pi$", 0, "$\pi$", "$2\pi$"])
ax.set_xticks(np.linspace(-2*pi, 2*pi, 17), minor=True)
plt.xlabel("Phase [rad]", family='serif')

plt.ylim(-1.25,1.25)
plt.yticks(np.linspace(-1,1,5))
ax.set_yticks(np.linspace(-1,1,9), minor=True)
plt.ylabel("Intensity [arb. units.]", family='serif')

plt.title("A Fancy Plot", family='serif', size='xx-large')
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

plt.savefig("fancy_plot.png")