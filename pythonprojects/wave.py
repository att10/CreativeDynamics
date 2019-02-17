# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np

W= np.zeros((128,128))
V= np.copy(W)
eps= 0.9
W[60:68,60:68]= 1.0
for t in range(50): #smoothing
    Wold= np.copy(W)
    for i in range(1,127):
        for j in range(1,127):
            W[i,j]= (1-eps)*Wold[i,j] + eps*( Wold[i,j-1] + Wold[i,j+1] + Wold[i-1,j] + Wold[i+1,j] )/4.0

# Display it
plt.show()
plt.plot(W,linewidth=0.5)

plt.pause(0.0001)


mu= 1
eps= 0.1
for t in range(200000):
    Wold= np.copy(W)
    Vold= np.copy(V)
    for i in range(1,127):
        for j in range(1,127):
            ave= ( Wold[i,j-1] + Wold[i,j+1] + Wold[i-1,j] + Wold[i+1,j] )/4.0
            V[i,j]= Vold[i,j] + eps*mu*( ave - Wold[i,j] )
            W[i,j]= Wold[i,j] + eps* V[i,j]

    #print t
    plt.clf()
    plt.plot(W,linewidth=0.5)
    plt.pause(.00001)
