import matplotlib.pyplot as plt

w = 1920
h = 1080

axValues = []
bxValues = []
ayValues = []
byValues = []
iterVals = []

print('Let c = a + bi')
print('Enter a:')
cReal = float(input())
print('Enter b:')
cImag = float(input())
zoom = 0.8

for y in range(h):
    for x in range(w):
        real = 1.5 * (x-w/2) / (0.5*w*zoom)
        imag = (y-h/2) / (0.5*h*zoom)

        iter = 0
        max = 256

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
plt.scatter(axValues,ayValues, s=0.5, c=iterVals)
plt.scatter(bxValues,byValues, s=0.5, color="black")
plt.axis("off")
plt.show()
