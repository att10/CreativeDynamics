import matplotlib.pyplot as plt
import numpy as np
import math

def f(u,v):
    a= 0.75
    b= 0.0006
    rho= 17   # 1/epsilon
    return rho*u*(1.0-u)*(u-(v+b)/a)

def g(u,v):
    return u-v

N= 100
U= np.random.rand(N,N)
V= np.random.rand(N,N)
V[0,:]= V[-1,:] = 0
V[:,0]= V[:,-1] = 0
U[0,:]= U[-1,:] = 0
U[:,0]= U[:,-1] = 0
U[math.floor(N/2-6):math.floor(N/2+6),-1] = 0.95


# Display it
p = plt.imshow(U, interpolation='nearest',vmin=-0.1,vmax=0.1)
plt.set_cmap('winter')
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
    U[40:45,4] = 0.95
    U[80:85,6] = 0.95
    U[6,40:35] = 0.95
    U[30,45:50] = 0.95
    p.set_data(U)
    plt.pause(.00001)
