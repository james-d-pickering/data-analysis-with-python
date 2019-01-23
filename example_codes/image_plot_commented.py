import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#JDP note I have to import this new package matplotlib.image now!
import matplotlib.image as mpimg

plt.close('all')

#JDP from the mpimg package, i call the function imread, which turns my photo into
#JDP an array that I can easily plot using matplotlib
image = mpimg.imread("blue_tit.png")
#JDP the image I read in is 500x500 pixels and has three colour channels (RGB)
#JDP so the shape of the image array is (500,500,3) - i.e. 3 500x500 images, one
#JDP for each colour channel. When I define lum_image I only take one of these channels
lum_image = image[:,:,0]
#JDP here I set my colour map
colourmap = 'inferno'

fig = plt.figure()
#JDP the command imshow plots my image, the cmap argument sets the colourmap, and the
#JDP vmin and vmax arguments define the 'limits' of my colourmap - try changing them!
plt.imshow(lum_image, cmap=colourmap, vmin=0, vmax=1)
#JDP this turns off any axis labelling
plt.axis('off')
#JDP this adds a standard colourbar
plt.colorbar()
plt.savefig("image_plot.png")