#!/usr/bin/env python

#*********************************************************************
#Generalised nth order polynomial fitting code (upto 10th order)
#Copyright: Thompson Research Group
#April 2019
#*********************************************************************

import math, sys
import numpy as np
from scipy.optimize import curve_fit
import argparse
parser = argparse.ArgumentParser(description='polynomial curve fitting')
parser.add_argument('-i',action='store',dest='inputfile',help='Inputfile')
parser.add_argument('-o',action='store',dest='outputfile',help='Outputfile')
parser.add_argument('-f',action='store',dest='func',choices=['1','2','3','4','5','6','7','8','9','10'],help='polynomial fit')
parser.add_argument('-a', nargs="*",dest='initial_guess', action='store',default=None, type=float,help='initial_guess')
parser.add_argument('-x', action='store', dest='xdata_column',default=0,type=int,help='Xdata column;Default=0')
parser.add_argument('-y', action='store', dest='ydata_column',default=1,type=int,help='Ydata column;Default=1')
args = parser.parse_args()

#**********************************************************
#                     Inputs
#**********************************************************

inputfile=args.inputfile
outputfile=args.outputfile
initial_guess=args.initial_guess
xcol=args.xdata_column
ycol=args.ydata_column

yfit = []
perr = []

#**********************************************************
#define the functions for polynomial fit (upto 10th order)
#**********************************************************

def func1(x,a,b):
       return a+b*x
def func2(x,a,b,c):
       return a + b*x + c*x**2
def func3(x,a,b,c,d):
       return a+b*x+c*x**2+d*x**3
def func4(x,a,b,c,d,e):
       return a+b*x+c*x**2+d*x**3+e*x**4
def func5(x,a,b,c,d,e,f):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5
def func6(x,a,b,c,d,e,f,g):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6
def func7(x,a,b,c,d,e,f,g,h):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7
def func8(x,a,b,c,d,e,f,g,h,i):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8
def func9(x,a,b,c,d,e,f,g,h,i,j):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8+j*x**9
def func10(x,a,b,c,d,e,f,g,h,i,j,k):
       return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8+j*x**9+k*x**10

#************************************************************
#                   dictionary of functions
#************************************************************

func={'1':func1, '2':func2, '3':func3, '4':func4, '5':func5, '6':func6, '7':func7, '8':func8, '9':func9, '10':func10}
polynomial=func[args.func]

#****************************************************************************
#curve fitting, read x and y data from the specified column of the input file
#****************************************************************************

xdata= np.genfromtxt(inputfile,dtype=float,usecols=(xcol),autostrip=True)
ydata=np.genfromtxt(inputfile,dtype=float,usecols=(ycol),autostrip=True)
popt, pcov = curve_fit(polynomial, xdata, ydata, p0=(initial_guess))

#***************************************************************************
#         fitted data, error calculation and standard deviation
#***************************************************************************

yfit = polynomial(xdata,*popt)
n=len(xdata)
perr = np.sqrt(np.diag(pcov))
Std_dev=np.sqrt(np.sum((polynomial(xdata,*popt)-ydata)**2)/n)

#***********************************************************
#                  create a list of parameters
#***********************************************************

parameters=[]
nparameters=len(popt)
parameters.append('# parameters')
parameters.append(' ')
for p in range(nparameters):
    parameters.append(popt[p])
parameters.append(' ')
parameters.append('# error')
parameters.append(' ')
for p in range(nparameters):
    parameters.append(perr[p])
parameters.append(' ')
parameters.append('# standard deviation ')
parameters.append(' ')
parameters.append(Std_dev)

#******************************************
#         save parameters to file
#******************************************

print('# Number of data points = ',n)
with open('parameters.dat', 'w') as f:
    for item in parameters:
        f.write("%s\n" % item)
#print('# E = ',popt[0],popt[1])
#print('# a err = ',perr[0],perr[1])

#***************************************************
#         save fitted values in a different file
#***************************************************
np.savetxt(outputfile, np.transpose([xdata,yfit]),fmt=['%10.5f','%10.5f'])
