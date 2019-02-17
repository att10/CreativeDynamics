# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np



A= np.random.rand(128,128)
A[:,:]= 0.0
A[30:40,0] = 100
A[-1,115:120]= -100
A[0,70:80]= -100
A[60:80,-1]= 100


# Display it
p = plt.imshow(A, interpolation='nearest')
plt.set_cmap('OrRd')
plt.pause(1)

eps= 0.9
for t in range(200000):
    Aold= np.copy(A)
    """A[1:-2,1:-2] =  (1-eps)*Aold[1:-2,1:-2] + eps*( A[0:-3,1:-2]+A[2:-1,1:-2]+A[1:-2,0:-3]+A[1:-2,2:-1])/4.0
    """
    #Same as: ???
    for i in range(1,127):
        for j in range(1,127):
            A[i,j]= (1-eps)*Aold[i,j] + eps*( Aold[i,j-1] + Aold[i,j+1] + Aold[i-1,j] + Aold[i+1,j] )/4.0

    A[:,0]   = A[:,1]
    A[:,-1] = A[:,-2]
    A[0,:]   = A[1,:]
    A[-1,:] = A[-2,:]

    A[30:100,0] = 100
    A[-1,115:120]= -100
    A[0,70:80]= -100
    A[60:80,-1]= 100


    #print t
    p.set_data(A)
    plt.pause(.01)
    
