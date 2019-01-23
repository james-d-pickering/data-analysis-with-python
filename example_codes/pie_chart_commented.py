import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

#JDP loading in the data from a text file - make sure this file is in the same
#JDP folder as the pie_chart.py file!
seats = np.loadtxt("pie_chart.txt")
#JDP defining a list of labels for each segment of the pie chart
pie_labels = "Conservative","Liberal Democrat","Labour","Vacant"
#JDP making an array to define how much to offset each segment of the pie chart
explode = np.array([0,0.1,0,0])

fig = plt.figure()
#JDP plotting the pie chart - with all arguments as before. shadow=True just makes
#JDP it look a bit cooler, and the startangle rotates it into a nice orientation.
plt.pie(seats, labels=pie_labels, explode=explode, shadow=True, startangle=45)
#JDP axis(equal) makes the x and y axes equal, as a square, so the pie chart is
#JDP circular, not elliptical.
plt.axis("equal")
plt.title("Leicestershire County Council", fontsize="x-large")
plt.savefig("pie_chart.png")