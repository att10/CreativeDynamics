import matplotlib.pyplot as plt
import numpy as np
import math

x = -0.5
y = 0.2


n = 100000
zLine = [0] * n
xValues = []
yValues = []
aValues = [100]
bValues = [10]
epsilon = 0.001

def logistic(x, ep):
    return x + ep * (1 - (2 * x))

def predator(x, y, ep, birth, death):
    return y + (ep * ((-1 * y * death) + (birth * x * y)))

def prey(x, y, ep, birth, death):
    return x + (ep * (birth * x - (death * x * y)))

def graph(x,n,xValues, ep):
    for i in range(n):
        xValues.append(x)
        x = logistic(x, ep)

def predprey(n, aValues, bValues, ep):
    for i in range(n):
        aNew = prey(aValues[i],bValues[i], ep, 1, 1)
        bNew = predator(aValues[i],bValues[i], ep, 0.1, 1.2)
        aValues.append(aNew)
        bValues.append(bNew)

# graph(x, 10000, xValues, epsilon)
# graph(y, 10000, yValues, epsilon)
# plt.plot(xValues, linewidth=1, color="green")
# plt.plot(yValues, linewidth=1, color="orange")

plt.plot(zLine, linewidth=0.5, color="gray")

predprey(n, aValues, bValues, epsilon)
plt.plot(aValues, linewidth=1, color="blue")
plt.plot(bValues, linewidth=1, color="red")
#plt.plot(aValues, bValues, linewidth=1, color="orange")

plt.show()
