import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gs

plt.close('all')

image = mpimg.imread("blue_tit.png")
lum_image = image[:,:,0]

#JDP to make the loop work I have to define a counter so i can increment through my 
#JDP colourmaps vector.
colour_count = -1
#JDP here I list all 9 different colourmaps
colourmaps = ('inferno', 'viridis', 'rainbow', 'jet', 'bone', 'spring', 'spectral', 'seismic', 'BrBG')

plt.figure(figsize(7,7))

grid = gs.GridSpec(nrows=3,ncols=3)

#JDP see if you can work out how this loop works. Try to print i and j as it runs
#JDP and get a feel for how it works. Why do I need the colour_count variable?
for i in range(0,3):
    for j in range(0,3):
        colour_count = colour_count + 1
        ax = plt.subplot(grid[i,j])
        ax.axis('off')
        ax.imshow(lum_image, cmap=colourmaps[colour_count])

plt.savefig('ex_3_q_3.png')

