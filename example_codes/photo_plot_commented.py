import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#JDP importing a new package - matplotlib.image
import matplotlib.image as mpimg

plt.close('all')
#JDP reading in my image so it can be plotted
image = mpimg.imread("blue_tit.png")

fig = plt.figure()
#JDP simply using the plt.imshow command to show my photo!
plt.imshow(image)
#JDP turning off axis labels so we only get a photo, and not any x or y labels.
plt.axis('off')
plt.savefig("photo_plot.png")