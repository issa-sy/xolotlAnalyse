#!/usr/bin/env python
#=======================================================================================
# xenonPlotting.py
# Plots the xenon retention values obtained with Xolotl
#=======================================================================================

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

## Create plots
fig1 = plt.figure()
densityPlot = plt.subplot(111)

# Chargement du premier fichier
time1, I1, V1, Xe1,Xe1V1,Xe1V2 = loadtxt('retentionOut.txt', usecols = (0,2,3,5,6, 7) , unpack=True)
# Chargement du deuxième fichier (à adapter selon ton chemin et tes colonnes)
time2, I1_2 = loadtxt('I.txt', usecols=(0, 1), unpack=True)
time3, V1_2 = loadtxt('V.txt', usecols=(0, 1), unpack=True)
time4, Xe1_2 = loadtxt('Xe.txt', usecols=(0, 1), unpack=True)
time5, V1_Xe1_2 = loadtxt('VXe.txt', usecols=(0, 1), unpack=True)
time6, V2_Xe1_2 = loadtxt('V2Xe.txt', usecols=(0, 1), unpack=True)


# Tracé du fichier 1
densityPlot.plot(time1, 10e21*I1, lw=3, color='orange', ls='-', label='I', alpha=0.7)
densityPlot.plot(time1, 10e21*V1, lw=3, color='blue', ls='-', label='V', alpha=0.7)
densityPlot.plot(time1, 10e21*Xe1, lw=3, color='black', ls='-', label='Kr', alpha=0.7)
densityPlot.plot(time1, 10e21*Xe1V1, lw=3, color='green', ls='-', label='VKr', alpha=0.7)
densityPlot.plot(time1, 10e21*Xe1V2, lw=3, color='red', ls='-', label='V$_2$Kr', alpha=0.7)


# Tracé du fichier 2 (avec styles différents pour différencier)
densityPlot.plot(time2, I1_2, lw=3, color='orange', ls='--', alpha=0.7)
densityPlot.plot(time3, V1_2, lw=3, color='blue', ls='--', alpha=0.7)
densityPlot.plot(time4, Xe1_2, lw=3, color='black', ls='--', alpha=0.7)
densityPlot.plot(time5, V1_Xe1_2, lw=3, color='green', ls='--', alpha=0.7)
densityPlot.plot(time6, V2_Xe1_2, lw=3, color='red', ls='--', alpha=0.7)

## Légende
l = densityPlot.legend(loc="best")
setp(l.get_texts(), fontsize=15)

## Mise en forme
densityPlot.set_xlabel("Time (s)", fontsize=20)
densityPlot.set_ylabel("Concentration (cm$^{-3}$)", fontsize=20)
densityPlot.set_xscale('log')
densityPlot.set_yscale('log')
densityPlot.grid()
densityPlot.tick_params(axis='both', which='major', labelsize=15)
densityPlot.tick_params(axis='both', which='minor', labelsize=10)

## Affichage
plt.tight_layout()
plt.show()
