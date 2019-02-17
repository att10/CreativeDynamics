import random
import matplotlib.pyplot as plt

ep = 0.000001

def getX(x, y, a, b):
    return x + ep * (a * x + b * y)

def getY(x, y, c, d):
    return y + ep * (c * x + d * y)

def start(x, y, a, b, c, d):

    xVals = [getX(x, y, a, b)]
    yVals = [getY(x, y, c, d)]
    graph(a, b, c, d, xVals, yVals)

def graph(a, b, c, d, xVals, yVals):
    for i in range(100000):
        xNew = getX(xVals[i], yVals[i], a, b)
        yNew = getY(xVals[i], yVals[i], c, d)
        xVals.append(xNew)
        yVals.append(yNew)
    plt.plot(xVals, yVals, linewidth=0.7)
    #plt.plot(, linewidth=1)

def loop():
    a = random.uniform(-10.0, 10.0)
    b = random.uniform(-10.0, 10.0)
    c = random.uniform(-10.0, 10.0)
    d = random.uniform(-10.0, 10.0)
    for i in range(500):
        start(random.uniform(-1,1), random.uniform(-1,1), a, b, c, d)

loop()
plt.show()
