# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np

W= np.zeros(128)
V= np.copy(W)
eps= 0.9
W[60:68]= 1
for t in range(50): #smoothing
    Wold= np.copy(W)
    for i in range(1,127):
        W[i]= (1-eps)*Wold[i] + eps*( Wold[i-1] + Wold[i+1] )/2.0

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
        ave= (Wold[i-1] + Wold[i+1] )/2.0
        V[i]= Vold[i] + eps*mu*( ave - Wold[i] )
        W[i]= Wold[i] + eps* V[i]

    #print t
    plt.clf()
    plt.plot(W,linewidth=0.5)
    plt.pause(.00001)
