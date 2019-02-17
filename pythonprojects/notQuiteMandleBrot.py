import matplotlib.pyplot as plt
import math

w = 1080
h = 720

axValues = []
bxValues = []
ayValues = []
byValues = []
iterVals = []

zoom = 0.9

for y in range(h):
    for x in range(w):
        cReal = 1.5 * (x-w/2) / (0.5*w*zoom)
        cImag = (y-h/2) / (0.5*h*zoom)
        real = 0
        imag = 0
        iter = 0
        max = 300

        while ((((real*real) + (imag*imag))) < 4) and iter < max:
            rTemp = real
            iTemp = imag

            real = (rTemp*rTemp*rTemp) - (3*rTemp*iTemp*iTemp) + cReal
            imag = (3*rTemp*rTemp*iTemp) - (iTemp*iTemp*iTemp) + cImag

            iter += 1


        if iter < max:
            axValues.append(x)
            ayValues.append(y)
            iterVals.append(math.log(iter))
        else:
            bxValues.append(x)
            byValues.append(y)

print('now plotting...')
plt.figure(dpi=150)
plt.scatter(axValues,ayValues,1, c=iterVals)
plt.scatter(bxValues,byValues,1, color="black")
plt.axis("off")
plt.show()
