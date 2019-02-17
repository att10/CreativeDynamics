# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def f(u,v):
    a= 0.75
    b= 0.002
    rho= 22   # 1/epsilon
    return rho*u*(1.0-u)*(u-(v+b)/a)

def g(u,v):
    return u-v

def wrap(A):
    # wrap
    A[:,0]= A[:,-4]
    A[:,1]= A[:,-3]

    A[:,-2]= A[:,2]
    A[:,-1]= A[:,3]

    A[0,:]= A[-4,:]
    A[1,:]= A[-3,:]

    A[-2,:]= A[2,:]
    A[-1,:]= A[3,:]

    return A


N= 128
U= np.random.rand(N,N)
V= np.random.rand(N,N)
wrap(U)
wrap(V)

U[math.floor(N/2-9):math.floor(N/2+3),math.floor(N/2-6):math.floor(N/2+6)] = 0.95
V[math.floor(N/2-6):math.floor(N/2+6),math.floor(N/2-8):math.floor(N/2+4)] = 0.95


# Display it
p = plt.imshow(U, interpolation='nearest',vmin=-0.1,vmax=0.1)
plt.set_cmap('winter')
plt.pause(1)


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
    wrap(U)
    wrap(V)
    if t<40:
        U[math.floor(N/2-9):math.floor(N/2+32),math.floor(N/2-6):math.floor(N/2+3)] = 0.95
        V[math.floor(N/2-6):math.floor(N/2+30),math.floor(N/2-4):math.floor(N/2+4)] = 0.95
#        U[N/2-6:N/2+6,N/2-6:N/2+6] = 0.95

    p.set_data(U)
    plt.pause(.0001)
