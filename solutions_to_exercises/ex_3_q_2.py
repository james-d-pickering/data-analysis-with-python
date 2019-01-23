import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gs

plt.close('all')

image = mpimg.imread("blue_tit.png")
lum_image = image[:,:,0]

plt.figure(figsize(7,7))

grid = gs.GridSpec(nrows=3,ncols=3,)

ax1 = plt.subplot(grid[0,0])
ax1.imshow(lum_image, cmap='inferno')
ax1.axis('off')

ax2 = plt.subplot(grid[1,0])
ax2.imshow(lum_image, cmap='viridis')
ax2.axis('off')

ax3 = plt.subplot(grid[2,0])
ax3.imshow(lum_image, cmap='rainbow')
ax3.axis('off')

ax4 = plt.subplot(grid[0,1])
ax4.imshow(lum_image, cmap='jet')
ax4.axis('off')

ax5 = plt.subplot(grid[1,1])
ax5.imshow(lum_image, cmap='bone')
ax5.axis('off')

ax6 = plt.subplot(grid[2,1])
ax6.imshow(lum_image, cmap='spring')
ax6.axis('off')

ax7 = plt.subplot(grid[0,2])
ax7.imshow(lum_image, cmap='spectral')
ax7.axis('off')

ax8 = plt.subplot(grid[1,2])
ax8.imshow(lum_image, cmap='seismic')
ax8.axis('off')

ax9 = plt.subplot(grid[2,2])
ax9.imshow(lum_image, cmap='BrBG')
ax9.axis('off')

plt.savefig('ex_3_q_2.png')

