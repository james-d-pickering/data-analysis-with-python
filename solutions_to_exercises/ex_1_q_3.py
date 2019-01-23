import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')
#JDP initialising variables, now I make multiple y variables and define x from
#JDP 0 to 360 not 0 to 2pi.
pi = 3.14159
x = np.linspace(0, 360, 50)
#JDP np.cos and np.sin need the x argument in radians, so we convert it.
y = np.cos(x*(pi/180))
y2 = np.sin(x*(pi/180))


#JDP Now adding multiple plt.plot commands, and changing xlim to 0 to 360.
fig = plt.figure()
plt.plot(x, y, color='black')
plt.plot(x, y2, color='blue')
plt.xlim(0, 360)
plt.xlabel('x [deg]')
plt.ylabel('y')
plt.title('Assorted Trig Functions in Degrees')
plt.grid('on')
plt.savefig('ex_1_q_3.png')