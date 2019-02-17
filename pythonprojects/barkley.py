import numpy as np
import matplotlib.pyplot as plt

N = 150

U = np.zeros((N,N))
V = np.zeros((N,N))

def f(u,v):
    a= 0.75
    b= 0.2
    e = 0.02
    return (1/e) * u * (1.0-u) * (u- ((v + b) / a))

def g(u,v):
    return u-v


# Display it
p = plt.imshow(U, interpolation='nearest',vmin=-0.1,vmax=0.1)
plt.set_cmap('summer')
plt.pause(0.00001)


deps= 0.1
eps= 0.1
for t in range(200000):
    # diffuse
    Uold= np.copy(U)
    for i in range(1,N-1):
        for j in range(1,N-1):
            U[i,j]= (1-eps)*Uold[i,j] + deps*( Uold[i,j-1] + Uold[i,j+1] + Uold[i-1,j] + Uold[i+1,j] )/4.0

    # react
    Uold= np.copy(U)
    Vold= np.copy(V)
    for i in range(1,N-1):
        for j in range(1,N-1):
            U[i,j]= Uold[i,j] + eps*f(Uold[i,j],Vold[i,j])
            V[i,j]= Vold[i,j] + eps*g(Uold[i,j],Vold[i,j])
    V[0,:]= V[-1,:] = 0
    V[:,0]= V[:,-1] = 0
    U[0,:]= U[-1,:] = 0
    U[:,0]= U[:,-1] = 0
    U[40:50,10] = 0.95
    U[60:65,55] = 0.95
    p.set_data(U)
    plt.pause(.00001)
