import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.close('all')

image = mpimg.imread("blue_tit.png")
lum_image = image[:,:,0]
colourmap = 'inferno'

fig = plt.figure()
plt.imshow(lum_image, cmap=colourmap, vmin=0, vmax=1)
plt.axis('off')
plt.colorbar()
plt.savefig("image_plot.png")