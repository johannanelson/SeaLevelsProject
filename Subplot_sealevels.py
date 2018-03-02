import csv
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pylab
from pylab import *


#Sea level versus year plot 

f = open("/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/NYC_sealevels.csv")
csv_f = csv.reader(f)
csv_f.next()

year = []
lev = []

for row in csv_f:
	year.append(float(row[0]))
	lev.append(float(row[3]))

plt.subplot(211)
plt.scatter(year, lev, c=lev, s=25)
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.title("New York Sea Level vs. Year")
plt.xlim([1926, 2012])
plt.ylim([500,2600])
(m,b) = polyfit(year, lev, 1)
yp = polyval([m,b], year)
grid(True)
plot(year,yp, "black", linewidth=3)


# CO2 emission versus year plot
f = open('/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/CO2_emissions.csv')
csv_f = csv.reader(f)
csv_f.next()

year2 = []
nyc = []
cali = []
texas = []


l_nyc = []
l_texas = []
l_cali = []

for row in csv_f:
	year2.append(float(row[1]))
	l_nyc.append(float(row[0]))
	nyc.append(float(row[0]))

plt.subplot(223)
plt.plot(year2, nyc,'darkmagenta', label="NYC", linewidth = 2.0)
grid(True)
plt.xlabel("Year")
plt.ylabel("State's CO2 Emission")
plt.title("Year vs. CO2 Emission")
plt.legend(loc="best", prop = {'size': 7})


# #Temperature versus year
f = open('/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/Temperature3.csv')
csv_f = csv.reader(f)
csv_f.next()

year3 = []
temp = []

for row in csv_f:
	year3.append(float(row[0]))
	temp.append(float(row[1]))

(m,b) = polyfit(year3, temp, 1)
yp = polyval([m,b], year3)

plt.subplot(224);
plt.title("Year vs. NYC temperature")
plt.xlabel("Year")
plt.ylabel("Temperature")
plot(year3,yp, "maroon", linewidth=2)
plt.scatter(year3,temp, c=temp, s=75)
plt.gray()
grid(True)


# plt.subplot(221);
# plt.plot(year,lev)
# 
# plt.subplot(222);
# plt.plot(year2,nyc)
# plt.plot(year2, cali)
# plt.plot(year2, texas)
# plt.legend(loc = "best")

# plt.subplot(223.5);
# plt.plot(year3,temp)
plt.show()