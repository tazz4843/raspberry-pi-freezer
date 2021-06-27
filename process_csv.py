# coding=utf-8
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

with open("output.csv") as f:
    reader = csv.reader(f)
    data = [i for i in reader]

x = [i[0] for i in data]
y0 = [float(i[1]) for i in data]
y1 = [float(i[2])/100 for i in data]
print(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title("Core Temperature and Speed vs Time")
ax.plot(x, y0, "r")
ax.plot(x, y1, "b")
loc = plticker.MaxNLocator(nbins=5)
plt.xlabel("Unix Timestamp")
plt.ylabel("Temp (deg C) and MHz*100")
ax.xaxis.set_major_locator(loc)
plt.show()
