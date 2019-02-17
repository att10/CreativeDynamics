import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad

#starting points
a = 0.10000001
b = 0.1
t = 0
epsilon = abs(a - b)
xValues = []
yValues = []

def iterate(z):
    return 4*z*(1-z)

def plotIter(xV, yV):
    plt.plot(xV,linewidth=1, color="blue")
    plt.plot(yV,linewidth=1, color="red")

def calcL(t, delta, epsilon):
    print("L0: " + str((1.0/t) * np.log(abs(delta/epsilon))))

def calcOtherL(t, xValues):
    solution = 0
    for x in xValues:
        solution += np.log(abs(4-(8*x)))
    print("L1: " + str( (1.0/(t+1)) * solution))

def begin(x,y,t, xValues, yValues, ep):
    print("Next Iteration? (y/n)")
    doPlot = input()

    if doPlot == "y":
        print("-----Iteration #" + str(t) + "-----")
        print("delta = " + str(x-y))

        plotIter(xValues,yValues)

        x = iterate(x)
        y = iterate(y)

        xValues.append(x)
        yValues.append(y)

        t += 1

        begin(x,y,t,xValues,yValues, ep)

    else:
        calcL(t, x-y, ep)
        calcOtherL(t, xValues)


begin(a,b,t, xValues,yValues, epsilon)
plt.show()
