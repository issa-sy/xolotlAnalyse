#!/usr/bin/env python
#=======================================================================================
# xenonPlotting.py
# Plots the xenon retention values obtained with Xolotl
#=======================================================================================

import numpy as np
import math
import matplotlib.pyplot as plt
from   pylab import *

## Create plots
fig1 = plt.figure()
densityPlot = plt.subplot(111)

time1, I1, V1, Xe1,Xe1V1,Xe1V2 = loadtxt('retentionOut.txt', usecols = (0,2,3,5,6,7) , unpack=True)

densityPlot.plot(time1, 10e21*I1, lw=4, color='orange', ls='-', label='I', alpha=0.7, marker='v')
densityPlot.plot(time1, 10e21*V1, lw=4, color='blue', ls='-', label='V', alpha=0.7, marker='s')
densityPlot.plot(time1, 10e21*Xe1, lw=4, color='black', ls='-', label='Kr', alpha=0.7, marker='p')
densityPlot.plot(time1, 10e21*Xe1V1, lw=4, color='green', ls='-', label='VKr', alpha=0.7, marker='h')
densityPlot.plot(time1, 10e21*Xe1V2, lw=4, color='red', ls='-', label='V$_2$Kr', alpha=0.7, marker='H')

## Plot the legend
l = densityPlot.legend(loc="best")
setp(l.get_texts(), fontsize=20)

## Some shaping
densityPlot.set_xlabel("Time (s)",fontsize=25)
densityPlot.set_ylabel("Concentration (cm$^{-3}$)",fontsize=25)
densityPlot.set_xscale('log')
densityPlot.set_yscale('log')
densityPlot.grid()
densityPlot.tick_params(axis='both', which='major', labelsize=25)
densityPlot.tick_params(axis='both', which='minor', labelsize=25)

## Show the plots
plt.show()
