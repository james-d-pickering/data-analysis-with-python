import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.close('all')

image = mpimg.imread("blue_tit.png")

fig = plt.figure()
plt.imshow(image)
plt.axis('off')
plt.savefig("photo_plot.png")