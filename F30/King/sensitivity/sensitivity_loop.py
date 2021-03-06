#!/usr/bin/python

import numpy as np
import os
import time

lower = 0.1
upper = 7
#timeStep = 
Nsteps = 10
obsNames = "TobiasThimo"

fileName1 = "sensitivity_I_1_"
fileName2 = "sensitivity_I_2_"
#times = np.arange(lower, upper, timeStep)
times = np.linspace(lower,upper,Nsteps)
for timex in times:
    os.system('ccdread -C 0 -b 2 -g 5 -T -F {fileName} -e {expTime} -o {fileName}{expTime} -u {obsNames} -O -C 1'.format(fileName=fileName1, expTime=str(timex), obsNames=obsNames))
    os.system('ccdread -C 0 -b 2 -g 5 -T -F {fileName} -e {expTime} -o {fileName}{expTime} -u {obsNames} -O -C 1'.format(fileName=fileName2, expTime=str(timex), obsNames=obsNames))
    print "Preparing for next pair of images - don't interrupt now!"

