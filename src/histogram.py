#!/usr/bin/env python
import numpy as np
import argparse
parser = argparse.ArgumentParser()


#Set up input flags
parser.add_argument('-i', action='store', dest='inputfile',required=True,help='Input Filename')
parser.add_argument('-o', action='store', dest='outputfile',required=True,help='Output Filename')
parser.add_argument('-c', action='store', dest='data_column',type=int,default=1,help='Column Index to Histogram, Starting at 0; Default=1')
parser.add_argument('-b', action='store', dest='nbins',type=int,default=100,help='# of Histogram bins; Default=100')
parser.add_argument('-r', action='store', nargs='*',dest='range',type=float,help='Range of values to include in Histogram')
parser.add_argument('-n', action='store_true',dest='normed',default=False,help='Turns on Normalization of Histogram; Default=off')

#Convert input flags to variables
args = parser.parse_args()

file_in=args.inputfile
file_out=args.outputfile
ncol=args.data_column
nbin=args.nbins
range=args.range
norm=args.normed

#Read in the data
ydata = np.genfromtxt(file_in,dtype=float,usecols=(ncol),autostrip=True)


#Histogram the data
hist = []
bin_edges = []
hist, bin_edges = np.histogram(ydata,bins=nbin,range=range,density=norm)

#Determine the bin centers
width = (bin_edges[1] - bin_edges[0])
center = (bin_edges[:-1] + bin_edges[1:]) / 2

#np.savetxt(file_out, np.transpose([center,hist]),fmt=['%10.5f','%10.5f'])
np.savetxt(file_out, np.transpose([center,hist]))
