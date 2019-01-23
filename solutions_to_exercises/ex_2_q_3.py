import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

#JDP loading in the text file and defining some constants
molecular_speeds = np.loadtxt('molecular_speeds.txt') 
k = 1.38E-23
T = 298
m = 28*1.6E-27

#JDP defining a vector of speeds to plot the idealised distribution
v = np.linspace(0,1500,500)

#JDP Making the Maxwell-Boltzmann distribution. The last line first normalises
#JDP it then scales it to fit the histogram. The number 60 was got by inspection
#JDP from the graph - quick and dirty but it works.
A = (m/(2*np.pi*k*T))**1.5
speeds_dist = A*np.exp(-(m*(v**2)/(2*k*T)))*v*v*4*np.pi
speeds_dist = (speeds_dist / np.max(speeds_dist))*60 

#JDP Plotting everything, using 50 bins for the histogram.
plt.figure()
plt.hist(molecular_speeds, 50, label='Histogram Data')
plt.plot(v, speeds_dist, label='Idealised Distribution')
plt.xlim(0, 1400)
plt.ylim(0,70)
plt.xlabel('Speed [m/s]')
plt.ylabel('Frequency')
plt.title('Maxwell-Boltzmann Distribution')
plt.legend()
plt.savefig('ex_2_q_3.png')