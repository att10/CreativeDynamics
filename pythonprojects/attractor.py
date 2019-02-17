import matplotlib.pyplot as plt
import numpy as np

ep = 0.03
x = 1
y = 1
z = 1
x1 = 1.00001
y1 = 1.00001
z1 = 1.00001
x2 = 0.99999
y2 = 0.99999
z2 = 0.99999


def getX(x, y, ep):
    return x + ep * ((-1 * y) - z)

def getY(x, y, z, ep):
    return y + ep * (x + (0.2 * y))

def getZ(x, y, z, ep):
    return z + ep * (0.2 + z * (x - 5.7))

def rotateX(x, z, angle):
    return (x * np.cos(angle)) + (z * np.sin(angle))

def rotateZ(x, z, angle):
    return (-1 * x * np.sin(angle)) + (z * np.cos(angle))

def rotateAll(xValues, zValues, angle):
    newXVals = []
    newZVals = []
    for i in range(len(xValues)):
        newXVals.append(rotateX(xValues[i], zValues[i], angle))
        newZVals.append(rotateZ(xValues[i], zValues[i], angle))
    return [newXVals, newZVals]


xValues = []
yValues = []
zValues = []
x1Values = []
y1Values = []
z1Values = []
x2Values = []
y2Values = []
z2Values = []
angle = 0.01

plt.figure(figsize=(7.5,7.5))

for i in range(10000):
    # plt.scatter(x,y,s=0.1, c="r")
    # plt.scatter(x1,y1,s=0.1, color="orange")

    xValues.append(x)
    yValues.append(y)
    zValues.append(z)
    x1Values.append(x1)
    y1Values.append(y1)
    z1Values.append(z1)
    x2Values.append(x2)
    y2Values.append(y2)
    z2Values.append(z2)


    xN = getX(x, y, ep)
    yN = getY(x, y, z, ep)
    zN = getZ(x, y, z, ep)
    x1N = getX(x1, y1, ep)
    y1N = getY(x1, y1, z1, ep)
    z1N = getZ(x1, y1, z1, ep)
    x2N = getX(x2, y2, ep)
    y2N = getY(x2, y2, z2, ep)
    z2N = getZ(x2, y2, z2, ep)

    x = xN
    y = yN
    z = zN

    x1 = x1N
    y1 = y1N
    z1 = z1N

    x2 = x2N
    y2 = y2N
    z2 = z2N

    new = rotateAll(xValues, zValues, angle)
    rxValues = new[0]
    rzValues = new[1]
    new = rotateAll(x1Values, z1Values, angle)
    rx1Values = new[0]
    rz1Values = new[1]
    new = rotateAll(x2Values, z2Values, angle)
    rx2Values = new[0]
    rz2Values = new[1]
    angle += 0.01

    plt.clf()
    plt.axis("off")
    plt.plot(rxValues, yValues, linewidth=0.3, color="blue")
    plt.plot(rx1Values, y1Values, linewidth=0.3, color="cyan")
    plt.plot(rx2Values, y2Values, linewidth=0.3, color="purple")
    plt.pause(0.00000000001)



# plt.plot(xValues, yValues, linewidth=0.5, color="red")
# plt.plot(x1Values, y1Values, linewidth=0.5, color="orange")
plt.show()
