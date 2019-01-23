import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')
#JDP I now use the loadtxt function to load the numbers from the file 'heights.txt'
#JDP this just imports all the numbers in that file into an array I can use for plotting
heights = np.loadtxt("heights.txt")
#JDP this creates an array which defines how wide the bins are in my histogram
height_bins = np.array([3,4,5,6,7,8,9])
fig = plt.figure()

#JDP the plt.hist command creates the histogram - note that we don't have x and y, 
#JDP but rather heights, and the height_bins argument that tells us how wide the bins are
plt.hist(heights, bins=height_bins)
#JDP the rest below should be familiar!
plt.xlim(3,9)
plt.ylim(0,9)
plt.xlabel("Height of trees [ft]")
plt.ylabel("Number of trees")
plt.title("A Simple Histogram")
#JDP here I add the argument axis='x', so i only plot grid lines from the x axis.
plt.grid("on", axis="x")
plt.savefig("simple_histogram.png")