import sys
import numpy as num
import pylab as py
import math
import os

#reading in the file and creating an array for the data
file = raw_input('filename')
datafile = open(file)
data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
data = data[num.isfinite(data)]

k = len(data)
j = len(data)/2
ID = num.array(data[0:j:3])
IDX = num.array(data[1:j:3])
IDY = num.array(data[2:j:3])
OD = num.array(data[j:k:3])
ODX = num.array(data[j+1:k:3])
ODY = num.array(data[j+2:k:3])

#ID_nom = 0.165
#OD_nom = 2.154

ID_err = 0.165 - ID
OD_err = 2.154 - OD
Concentricity = (((IDX-ODX)**2)+((IDY-ODY)**2))**0.5

for i in range (0,k):
    if ID_err[i] < -0.004:
        print 'ID Err >'
        print i
    if ID_err[i] > 0.003:
        print 'ID Err <'
        print i
        print
    if OD_err[i] > 0.03:
        print 'OD Err >'
        print i
    if OD_err[i] < -0.03:
        print 'OD Err <'
        print i
    if Concentricity[i] > 0.03:
        print 'Conc Err'
        print i

f = open('sky.txt', 'w+')

for i in range (0,k):
    f.write('%i\t%f\t%f\t%f\n'%(i+1,ID_err[i],OD_err[i],Concentricity[i]))
    
f.close()
