import csv
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pylab
from pylab import *


#nyc sea levels

f = open("/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/Sea_levels/NYCsealevel.csv")
csv_f = csv.reader(f)
csv_f.next()

year = []
lev = []

for row in csv_f:
	year.append(float(row[0]))
	lev.append(float(row[1]))

plt.subplot(221);
plt.scatter(year, lev, c=lev, s=25)
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.ylim([-.7,.2])
plt.title("New York Sea Level vs. Year")
plt.xlim([1900, 2020])
plt.gray()
grid(True)


#cali sea levels

f = open("/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/Sea_levels/Calisealevel.csv")
csv_f = csv.reader(f)
csv_f.next()

year = []
lev = []

for row in csv_f:
	year.append(float(row[0]))
	lev.append(float(row[1]))

plt.subplot(223);
plt.scatter(year, lev, c=lev, s=25)
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.ylim([-.7,.2])
plt.title("Cali Sea Level vs. Year")
plt.xlim([1900, 2020])
plt.gray()
grid(True)


#texas sea levels

f = open("/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/Sea_levels/TexasSeaLevels.csv")
csv_f = csv.reader(f)
csv_f.next()

year = []
lev = []

for row in csv_f:
	year.append(float(row[0]))
	lev.append(float(row[1]))

plt.subplot(224);
plt.scatter(year, lev, c=lev, s=25)
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.ylim([-.7,.2])
plt.title("Texas Sea Level vs. Year")
plt.xlim([1900, 2020])
plt.gray()
grid(True)


f = open("/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/CO2_emissions.csv")
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

plt.subplot(222)
plt.plot(year2, texas,'darkolivegreen', label = "Texas", linewidth = 2.0)
plt.plot(year2, cali, 'darkcyan', label = "California", linewidth = 2.0)
plt.plot(year2, nyc,'darkmagenta', label="NYC", linewidth = 2.0)
grid(True)
plt.xlabel("Year")
plt.ylabel("State's CO2 Emission")
plt.title("Year vs. CO2 Emission")
plt.legend(loc="best", prop = {'size': 7})

plt.show()