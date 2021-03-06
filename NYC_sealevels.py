import csv
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pylab
from pylab import *


#Sea level versus year plot 

f = open("/Users/johannanelson/desktop/NYC_sealevels.csv")
csv_f = csv.reader(f)
csv_f.next()

year = []
lev = []

for row in csv_f:
	year.append(float(row[0]))
	lev.append(float(row[3]))

plt.plot(year, lev, '*')
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.title("New York Sea Level vs. Year")
plt.xlim([1926, 2012])
plt.show()



# CO2 emission versus year plot
f = open('/Users/johannanelson/desktop/CO2_emissions.csv')
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
	l_texas.append(float(row[2]))
	texas.append(float(row[2]))
	l_cali.append(float(row[3]))
	cali.append(float(row[3]))

plt.plot(year2, nyc,'darkorchid', label="NYC")
plt.plot(year2, texas,'steelblue', label = "Texas")
plt.plot(year2, cali, 'seagreen', label = "California")
plt.xlabel("Year")
plt.ylabel("State's CO2 Emission")
plt.title("Year vs. CO2 Emission")
plt.legend(loc="best")
plt.show()


#Temperature versus year
f = open('/Users/johannanelson/desktop/Temperature3.csv')
csv_f = csv.reader(f)
csv_f.next()

year3 = []
temp = []

for row in csv_f:
	year3.append(float(row[0]))
	temp.append(float(row[1]))

(m,b) = polyfit(year3, temp, 1)
yp = polyval([m,b], year3)

plt.title("Year vs. NYC temperature")
plt.xlabel("Year")
plt.ylabel("Temperature")
plot(year3,yp, "plum")
scatter(year3,temp)
grid(True)
plt.show()







# plt.subplot(221);
# plt.plot(year,lev)
# 
# plt.subplot(222);
# plt.plot(year2,nyc)
# 
# plt.subplot(223);
# plt.plot(year3,temp)
# plt.show()