import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')
#JDP load data from files - note the square brackets at the end. This tells 
#JDP python to load the wavelengths from column one of the file and the absorption
#JDP data from column two.
wavelengths = np.loadtxt('benzene_UV_spectrum.txt')[:,0]
absorptions = np.loadtxt('benzene_UV_spectrum.txt')[:,1]
#JDP Just normalising the absorptions as the values are tiny otherwise
absorptions = absorptions/np.max(absorptions)

#JDP plotting things - note the kwarg 's' in scatter for the marker size.
plt.figure()
plt.scatter(wavelengths, absorptions, marker='x', s=10)
plt.plot(wavelengths, absorptions, linewidth=1)
plt.xlim(120,190)
plt.ylim(0,)
plt.xlabel('Wavelength [nm]')
plt.ylabel('Absorption')
plt.title('UV Absorption Spectrum of Benzene')
plt.grid('on')
plt.savefig('ex_2_q_1.png')