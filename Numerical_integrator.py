#!/usr/bin/env python
"""
Numerically integrate data

Need:
    xdata (or column in datafile)
    ydata (or column in datafile)
    integration method ()
    cumulative (start and stop points for the integrand)
    datafile
    outfile
    paramfile

For later
    numerical error
"""


# In[2]:

import numpy as np
import argparse
import scipy.integrate as numint


# In[52]:

parser = argparse.ArgumentParser(description="Perform numerical integration")
parser.add_argument('-x', '--x_col', type=int, help="Column number (indexed from zero) of the x data")
parser.add_argument('-y', '--y_col', type=int, help="Column number (indexed from zero) of the integrand")
parser.add_argument('-i', '--input', required=True, type=str, help="Path to the file with x and y data")
parser.add_argument('-o', '--output', default='integrate_out.dat', type=str, help="Path to the output file")
parser.add_argument('-m', '--method', default='trapz', type=str, choices=['trapz','cum','simps'],
                    help="Numerical integration method to use: must be trapz, cum, or simps. Default is trapz")
parser.add_argument('-l', '--limits', type=int, nargs='*', default=[0], help="Index(es) (from zero) of the lower and upper (inclusive) bounds of the integral.")
parser.add_argument('-s', '--sep', type=str, default=None, help="Separator used in the input file")


# In[60]:

args = parser.parse_args()


# In[61]:

infile = args.input
sep = args.sep
x = args.x_col
y = args.y_col
start = args.limits[0]

method_dict = {"trapz":numint.trapz, "cum":numint.cumtrapz, "simps":numint.simps}

integrator = method_dict[args.method]
data = np.genfromtxt(infile, delimiter=sep)

if len(args.limits) == 1:
    stop = data.shape[0]
else:
    stop = args.limits[1]+1


# In[67]:

integral = integrator(data[start:stop,y],data[start:stop:,x])

if args.method == 'cum':
    output = np.vstack((data[start+1:stop,x],integral)).T
    np.savetxt(args.output, output)
else:
    with open(args.output, 'w') as file:
        file.write(f'{data[start,x]:.12f}:{data[stop,x]:.12f}\t{integral:.12f}')


# In[ ]:
