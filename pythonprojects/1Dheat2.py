# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np



A= np.zeros(128)
A[30:60] = 100

# Display it
plt.figure()
plt.xlim(0,128)
plt.ylim(0,105)
plt.plot(A,'b')
plt.pause(1)

eps= 0.6
for t in range(200000):
    Aold= np.copy(A)
    for i in range(1,127):
        A[i]= (1-eps)*Aold[i] + eps*( Aold[i-1] + Aold[i+1])/2.0

    A[0]   = A[1]
    A[-1] = A[-2]

    #print t
    plt.clf()
    plt.xlim(0,128)
    plt.ylim(0,105)
    plt.plot(A,'b')
    plt.pause(.01)
