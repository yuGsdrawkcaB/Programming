# A program that takes a csv file containing raw sensor data for two trials from a titration and constructs 2 graphs for each trial
# Graph 1 is

# Trial 1 data is Run 2 and Trial 2 data is Run 3 on csv file

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
#Change for other trial 2
trial = 2

Kw = 1e-14
V0 = 0

#Filepath to the csv file
filepath = "C:\\Users\\tyler\\Programming\\PublicProjects\\Chemistry1021\\Lab6\\Trial1data.csv"
with open(filepath, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    datalist = []
    for row in csvreader:
        datalist.append(row)

for data in datalist:
    # x is delivered volume
    if data['Fluid Volume (mL) Run 3'] == '':
        continue
    x.append(float(data['Fluid Volume (mL) Run 3'])-V0)
    # y is pH values
    y.append(float(data['pH Run 3']))

input("press enter for volume vs pH graph")

xarray = np.array(x)
yarray = np.array(y)

plt.scatter(xarray, yarray, color='black')

plt.grid(True)

plt.xlabel('Delivered volume [V] (mL)')
plt.ylabel('pH value [pH] (-)')
plt.title(f'pH-versus-delivered-NaOH-volume graph Trial {trial}')

plt.savefig('all_features_plot.png')
plt.show()


slopes = []
midpoints = []

maxslope=0
x1_maxslope = 0
x2_maxslope = 0
y1_maxslope = 0
y2_maxslope = 0

for iter in range(0,len(x)-1):
    xcurrent = x[iter]
    xnext = x[iter+1]
    ycurrent = y[iter]
    ynext = y[iter+1]
    if xcurrent == xnext:
        continue
    slope = (ynext-ycurrent)/(xnext-xcurrent)
    slopes.append(slope)
    if slope > maxslope:
        maxslope = slope
        x1_maxslope = xcurrent
        x2_maxslope = xnext
        y1_maxslope = ycurrent
        y2_maxslope = ynext
    midpoint = (xnext+xcurrent)/2
    midpoints.append(midpoint)

sarray = np.array(slopes)
mparray = np.array(midpoints)

input("press enter for slope vs midpoint graph")

plt.scatter(mparray, sarray, color='blue')

plt.grid(True)

plt.xlabel('Midpoint')
plt.ylabel('Slope (pH units per mL)')
plt.title(f'Slopes vs Midpoints Trial {trial}')

plt.savefig('all_features_plot.png')
plt.show()


print(f"Value of steep main rise that occurs is {maxslope} and occurs between ({x1_maxslope},{y1_maxslope}) and ({x2_maxslope},{y2_maxslope})")

Veq = (x1_maxslope+x2_maxslope)/2
Vhalf = Veq/2
print(f"Veq = {Veq}")
print(f"Vhalf = {Vhalf}")


#ADJUST AFTER DATA COLLECTED
pH1 = 4.3307
pH2 = 4.3704
V1 = 8.921
V2 = 9
pHhalf = 4.3101
Ka = 10**-pHhalf
print(f"pHhalf = {pHhalf}")
print(f"pHhalf approx. = pKa")
print(f"Ka = {Ka}")
print(f"Kb = {Kw/Ka}")

MNaOH = 0.1
nHA = MNaOH * (Veq/1000)
MCA = nHA/0.02

print(f"MCA = {MCA}")