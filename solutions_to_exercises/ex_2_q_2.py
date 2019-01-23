import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

#JDP found the isotopes from wiki - in order of increasing atomic mass
lead_isotopes = ([1.4, 24.1, 22.1, 52.4])
lead_masses = ('$^{204}$Pb','$^{206}$Pb','$^{207}$Pb','$^{208}$Pb')

#JDP explode out the second least abundant segment
explode = ([0, 0.1, 0, 0])

#JDP plotting everything - remember axis equal or it looks weird!
plt.figure()
plt.pie(lead_isotopes, labels=lead_masses, explode=explode, shadow=True, startangle=0)
plt.axis('equal')
plt.title('Isotopes of Lead', fontsize='x-large')
plt.savefig("ex_2_q_2.png")