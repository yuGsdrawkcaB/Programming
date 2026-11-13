# A program that takes a csv file containing raw sensor data for two trials from a titration and constructs 2 graphs for each trial
# Graph 1 is fluid volume added vs pH of the solution
# Graph 2 is slopes between two points vs midpoints between the same two points

# Trial 1 data is Run 2 and Trial 2 data is Run 3 on csv file

import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
# Change for other trial 2
trial = 2

# Equilibrium constant of pure water
Kw = 1e-14
# Initial Volume
V0 = 0

#Filepath to the csv file
filepath = "PublicProjects\\Chemistry1021\\Lab6\\Trial1data.csv"
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

# Finds all slopes and midpoints between points, and checks every linear point combination for the maximum slope between points
# Variables are used instead of max() so the points with the greatest slope can be stored for later use
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

# Volume at the equivalence point
Veq = (x1_maxslope+x2_maxslope)/2
# Volume at the half equivalence point
Vhalf = Veq/2
print(f"Veq = {Veq}")
print(f"Vhalf = {Vhalf}")
