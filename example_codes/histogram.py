import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

heights = np.loadtxt("heights.txt")
height_bins = np.array([3,4,5,6,7,8,9])
fig = plt.figure()

plt.hist(heights, bins=height_bins)
plt.xlim(3,9)
plt.ylim(0,9)
plt.xlabel("Height of trees [ft]")
plt.ylabel("Number of trees")
plt.title("A Simple Histogram")
plt.grid("on", axis="x")
plt.savefig("simple_histogram.png")