# A program that creates a scatterplot for experimental values of the reaction rate constant, k, against experimental values of rate for a first-order reaction, t
# The data was gathered from the iodine clock reaction performed as part of Chemistry 1021 cirriculum
# An image of the table containing the neccessary data to construct the graph is included in the file

# ln(k) = -(Ea/R) * (1/T)
# Ideal Gas Constant (R) = 8.314
# Ea - Activation Energy for the reaction

import math
import numpy as np
import matplotlib.pyplot as plt

ln = lambda x: math.log(x)

#lists containing values of k and associated values of t from the lab data 
kvals = [0.0009, 0.0014, 0.00313, 0.0043, 0.0050, 0.0054, 0.0087]
tempvals = [285.25, 283.35, 298.15, 298.15, 303.05, 313.15, 312.65]

# Converts values of k into values of ln(k) using the previously defined lambda for ln
y = []
for k in kvals:
    y.append(ln(k))

# Converts values of t into values of 1/t
x = []
for T in tempvals:
    x.append(1/T)

#Creates a list of the final point values of (ln[k], 1/t) rounded to a reasonable number of digits
points = []
for num in range(0,len(y)):
    roundedx = round(x[num],5)
    roundedy = round(y[num],3)
    points.append(str((roundedx,roundedy)))

x = np.array(x)
y = np.array(y)
a, b = np.polyfit(x,y,1)

# Displays all points and the equation for the line of best fit
print("points (1/T, ln(k)): " + str(points))
print(f"Line of best fit is y = {b:.2f} + {a:.2f}x")
input("Press enter to continue to graph")

plt.scatter(x, y, color='red', label='(1/T, ln(k))')
plt.plot(x,a*x + b, color='black', label='Line of Best Fit')

plt.xlabel('1/T (K^-1)')
plt.ylabel('ln(k)')
plt.title('ln(k) vs 1/T graph')
plt.legend()
plt.show()

# Pauses program to allow the user to record the point values and line equation until user input is recieved
input("Press enter to continue to slope and Ea calculations")


print("slope = " + str(b))

# Ea = -(slope)R
Ea = float(-1 * b * 8.314)
print("Ea = " + str(Ea) + " kJ mol^-1")