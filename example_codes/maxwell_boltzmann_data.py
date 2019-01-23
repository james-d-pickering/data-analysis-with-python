#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:21:35 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.close('all')
k = 1.38E-23
T = 298
m = 28*1.6E-27

v = np.linspace(0,1500,5000)

A = (m/(2*np.pi*k*T))**1.5

speeds_dist = A*np.exp(-(m*(v**2)/(2*k*T)))*v*v*4*np.pi
speeds_dist /= speeds_dist.sum()

speeds_hist = np.random.choice(v, size=1000, p=speeds_dist)

np.savetxt('molecular_speeds.txt',speeds_hist)