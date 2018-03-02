import csv
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pylab
from pylab import *

f = open('/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/Temperature3.csv')
csv_f = csv.reader(f)
csv_f.next()
 
year3 = []
temp1 = []
 
#for row in csv_f:
#    year3.append(float(row[0]))
#    temp1.append(float(row[1]))
#
#(m,b) = polyfit(year3, temp1, 1)
#yp = polyval([m,b], year3)
# 
#plt.subplot(211);
#plt.title("Year vs. NYC temperature")
#plt.xlabel("Year")
#plt.ylabel("Temperature")
#plot(year3,yp, "maroon", linewidth=2)
#plt.scatter(year3,temp1, c=temp1, s=75)
#plt.gray()
#grid(True)
# 
# #California
#f = open('/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/calitemp.csv')
#csv_f = csv.reader(f)
#csv_f.next()
# 
#year4 = []
#temp2 = []
# 
#for row in csv_f:
#    year4.append(float(row[0]))
#    temp2.append(float(row[1]))
# 
#(m,b) = polyfit(year4, temp2, 1)
#yp = polyval([m,b], year4)
# 
#plt.subplot(223);
#plt.title("Year vs. California temperature")
#plt.xlabel("Year")
#plt.ylabel("Temperature")
#plot(year3,yp, "maroon", linewidth=2)
#plt.scatter(year3,temp2, c=temp2, s=75)
#plt.gray()
#grid(True)

#Texas
f = open('/Users/johannanelson/desktop/Bridge-Up/Sea-Levels-Project/texastemp.csv')
csv_f = csv.reader(f)
csv_f.next()

year3 = []
temp2 = []

for row in csv_f:
    year3.append(float(row[2]))
    temp2.append(float(row[1]))

(m,b) = polyfit(year3, temp, 1)
yp = polyval([m,b], year3)

plt.subplot(224);
plt.title("Year vs. NYC temperature")
plt.xlabel("Year")
plt.ylabel("Temperature")
plot(year3,yp, "maroon", linewidth=2)
plt.scatter(year3,temp2, c=temp2, s=75)
plt.gray()
grid(True)

plt.show()