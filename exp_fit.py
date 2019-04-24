#!/usr/bin/env python
import argparse
import math, sys
import numpy as np
from scipy.optimize import curve_fit

parser = argparse.ArgumentParser(description='Exponential Fits')

parser.add_argument('-exp', action="store", dest="var", help="number of exponentials to fit (integer)")
parser.add_argument('-p0', nargs="*", action="store", dest="guess", type=float, help="input initial guesses with spaces in between ex: a b c ... (float)")

args = parser.parse_args()
name = ['a =', 'b =', 'c =', 'd =', 'e =']
name_param = []
param = []
yfit = []
define = args.var
guesses = args.guess

def m_exp_1(x, a, b):
       return a*np.exp(-x/b)

def m_exp_2(x, a, b, c, d):
       return a*np.exp(-x/b) + c*np.exp(-x/d)

def m_exp_3(x, a, b, c, d, e):
       return a*np.exp(-x/b) + c*np.exp(-x/d) + (1-a-c)*np.exp(-x/e) 

exp_list = {
       '1': m_exp_1,
       '2': m_exp_2,
       '3': m_exp_3       
       }

filename = 'c2_rot_avg.dat'

xdata,ydata = np.genfromtxt(filename,dtype=float,usecols=(0,1),autostrip=True,unpack=True)
popt,pcov = curve_fit(exp_list[args.var], xdata, ydata, p0=guesses)

yfit = exp_list[args.var](xdata,*popt)

np.savetxt('m_exp_'+define+'.fits', np.transpose([xdata,yfit]),fmt=['%10.5f','%10.5f'],delimiter=' ')

length = len(popt)

for i in range(length):
       param.append(popt[i])
       name_param.append(name[i])

data = np.column_stack((name_param,param))
np.savetxt('param_'+define+'.dat', data, delimiter=' ', fmt='%s')
