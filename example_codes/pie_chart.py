import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')

seats = np.loadtxt("pie_chart.txt")
pie_labels = "Conservative","Liberal Democrat","Labour","Vacant"
explode = np.array([0,0.1,0,0])

fig = plt.figure()
plt.pie(seats, labels=pie_labels, explode=explode, shadow=True, startangle=45)
plt.axis("equal")
plt.title("Leicestershire County Council", fontsize="x-large")
plt.savefig("pie_chart.png")