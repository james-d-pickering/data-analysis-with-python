import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')
#JDP initialising variables, now I make multiple y variables.
pi = 3.14159
x = np.linspace(0, 2*pi, 50)
y = np.cos(x)
y2 = np.sin(x)
y3 = np.sin(x)**2

#JDP Now adding multiple plt.plot commands.
fig = plt.figure()
plt.plot(x, y, color='black')
plt.plot(x, y2, color='blue')
plt.plot(x, y3, color='red')
plt.xlim(0, 2*pi)
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.title('Assorted Trig Functions')
plt.grid('on')
plt.savefig('ex_1_q_2.png')