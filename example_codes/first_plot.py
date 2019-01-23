import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')

pi = 3.14159
x = np.linspace(0, 2*pi, 50)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y)
plt.xlim(0, 2*pi)
plt.xlabel('x [rad]')
plt.ylabel('sin(x)')
plt.title('A Simple Plot')
plt.grid('on')
plt.savefig('first_plot.png')