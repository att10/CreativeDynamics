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
A[0,70:80]= -100
A[-1,115:120]= -100


# Display it
p = plt.imshow(A, interpolation='nearest')
plt.set_cmap('OrRd')
plt.pause(2)


for t in range(2000):
        Aold= np.copy(A)
        for i in range(1,127):
            for j in range(1,127):
                A[i,j]= 0.9*Aold[i,j] + 0.1 * \
                        ( Aold[i+1,j-1] + Aold[i+1,j] + Aold[i+1,j+1] +
                          Aold[i  ,j-1]               + Aold[i  ,j+1] +
                          Aold[i-1,j-1] + Aold[i-1,j] + Aold[i-1,j+1]  )/8.0
        for i in range(127):
            A[i,0]   = A[i,1]
            A[i,-1] = A[i,-2]
            A[0,i]   = A[1,i]
            A[-1,i] = A[-2,i]

        for i in range(30,100):
            A[i,0]= 100

        for i in range(115,120):
            A[-1,i]= -100

        for i in range(70,80):
            A[0,i]= -100
        
        p.set_data(A)
        plt.pause(.01)
