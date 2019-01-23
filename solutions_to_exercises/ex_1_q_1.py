import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')
#JDP initialising variables - now only between 0 and pi
pi = 3.14159
x = np.linspace(0, pi, 50)
y = np.cos(x)

#JDP plotting things. Note I get the greek letter in the title with $\pi$. 
#JDP The reason for this is that matplotlib allows LaTeX formatting, this is
#JDP beyond what we want to discuss here. But know that you can other greek letters
#JDP in the same way.
fig = plt.figure()
plt.plot(x, y)
plt.xlim(0, pi)
plt.xlabel('x [rad]')
plt.ylabel('sin(x)')
plt.title('Cosine of x between 0 and $\pi$')
plt.grid('on')
plt.savefig('ex_1_q_1.png')