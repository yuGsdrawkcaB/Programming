# Part of an experiment performed in Chemistry 1021 focused around the reaction Fe³⁺(aq) + SCN⁻(aq) ⇌ FeSCN²⁺(aq)
# Involves calculating equilibrium concentrations of FeSCN²⁺ for a reaction by using varying, known concentrations of SCN⁻
# Absorbance is measured using a spectrometer to measure the solutions at equilibrium
# The program graphs absorbance of five solutions at equilibrium against the theoretical equilibrium concentration of FeSCN²⁺

import numpy as np
import matplotlib.pyplot as plt

## For Part A:

# Assigned FeSCN²⁺ concentrations in M
x = [2e-5, 4e-5, 8e-5, 1.2e-4, 1.6e-4]
# Measured absorbances
y = [0.4, 0.55, 0.57, 0.76, 0.94]

x = np.array(x)
y = np.array(y)

m, b = np.polyfit(x,y,1)

showgraph = input("Press enter to skip graph, input anything to show ")

if showgraph != "":
    print(f"Line of best fit is y = {b:.2f} + {m:.2f}x")


    plt.scatter(x, y, color='blue')
    plt.plot(x,m*x + b, color='red', label='Line of Best Fit')

    plt.xlabel('Assigned FeSCN²⁺ concentration in M')
    plt.ylabel('Measured absorbance')
    plt.legend()
    plt.show()

## For Part C:

#Absorbance for trials 1 through 3
a1 = 0.285
a2 = 0.325
a3 = 0.345
avals = [a1, a2, a3]

# Initial concentration of Fe³⁺ for all three trials
feinit = 1E-3
# Initial concentration of SCN⁻(aq) for each trial
scninit = [1E-4, 2E-4, 3E-4]

for a in avals:
    # reassigns values of a to the change in the concentration of FeSCN²⁺
    a = float((a-b)/m)

# Finds the change in molality and equilibrium concentration of the reactants for each trial 
# Also calculates the value of the reaction quotient at equilibrium, K, for each trial
iter = 0
for e in avals:
    feeq = feinit + e
    scneq = scninit[iter] + e
    print(f"x = " + str(e))
    print(f"[Fe]eq = " + str(feeq))
    print(f"[SCN]eq at E" + str(iter+1) + "= " + str(scneq))
    print(f"K at E" + str(iter+1) + "= " + str(e/(feeq*scneq)))
    iter += 1

