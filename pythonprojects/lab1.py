import matplotlib.pyplot as plt
import numpy as np

def iterateX(x, y):
    a = 1.4
    return 1 - (a * x * x) - y

def iterateY(x):
    b = 0.3
    return b * x

def plotIter(ax,ay,bx,by):
    plt.plot(ax,ay,linewidth=1, color="blue")
    plt.plot(bx,by,linewidth=1, color="red")

def begin(ax0,ay0,bx0,by0,axValues, ayValues,bxValues,byValues,t):
    print("Next Iteration? (y/n)")
    doPlot = input()
    if doPlot == "y":
        print("-----Iteration #" + str(t) + "-----")
        plotIter(axValues,ayValues,bxValues,byValues)
        ax = iterateX(ax0,ay0)
        ay = iterateY(ax0)
        bx = iterateX(bx0,by0)
        by = iterateY(bx0)
        axValues.append(ax)
        ayValues.append(ay)
        bxValues.append(bx)
        byValues.append(by)
        t+=1
        begin(ax,ay,bx,by,axValues,ayValues,bxValues,byValues,t)

axValues = []
ayValues = []
bxValues = []
byValues = []

t = 0

ax = 1.00000000000001
ay = 1.00000000000001
bx = 1
by = 1
begin(ax,ay,bx,by, axValues,ayValues, bxValues,byValues,t)
plt.show()
