import matplotlib.pyplot as plt

w = 3840
h = 2160

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

            real = (rTemp*rTemp) - (iTemp*iTemp) + cReal
            imag = (2 * rTemp * iTemp) + cImag

            iter += 1


        if iter < max:
            axValues.append(x)
            ayValues.append(y)
            iterVals.append(iter)
        else:
            bxValues.append(x)
            byValues.append(y)

print('now plotting...')
plt.figure(dpi=150)
plt.scatter(axValues,ayValues,1, c=iterVals)
plt.scatter(bxValues,byValues,1, color="black")
plt.axis("off")
plt.show()
