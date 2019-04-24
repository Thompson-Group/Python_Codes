#!/panfs/pfs.local/software/install/anaconda/4.3/envs/py36/bin/python

import numpy as np
from scipy import interpolate
import argparse
parser = argparse.ArgumentParser()


#Set up input flags
parser.add_argument('-i', action='store', dest='inputfile',required=True,help='Input Filename')
parser.add_argument('-o', action='store', dest='outputfile',required=True,help='Output Filename')
parser.add_argument('-c', action='store', dest='data_columns',nargs=2,type=int,default=[0,1],
                    help='x,y column indices to read; Default=(0,1)')
parser.add_argument('-m', action='store', dest='multiplier',type=int,default=2,
                    help='Factor to increase data density; Default=2')
parser.add_argument('-k', action='store', dest='method',choices=['linear','quadratic','cubic'],default='linear',
                    help='Type of interpolation method; Default=linear')

#Convert input flags to variables
args = parser.parse_args()

file_in=args.inputfile
file_out=args.outputfile
ncol=args.data_columns
mult=args.multiplier
method=args.method

#Read in the data
xdata=[]
ydata=[]
xdata, ydata = np.genfromtxt(file_in,dtype=float,usecols=ncol,autostrip=True,unpack=True)

ndata=len(xdata)
ninterp = (ndata-1)*mult+1

#Interpolate the data
f = interpolate.interp1d(xdata, ydata, kind=method)

#Generate a grid on which to evalulate the interpolation
x_interp = np.linspace(xdata[0],xdata[ndata-1],num=ninterp)

#Calculate the interpolated values
y_interp = f(x_interp)

#Write out the interpolated function
np.savetxt(file_out, np.transpose([x_interp,y_interp]))
