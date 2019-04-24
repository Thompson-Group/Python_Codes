#!/bin/bash

homepath=$(pwd)

if grep -q "module use $homepath/module" ~/.bash_profile ; then
    echo "module use already in bash profile"
else
    echo "module use $homepath/module" >> ~/.bash_profile
fi

if grep -q "prepend_path" module/Group_Python.lua ; then
    echo "modulefile updated"
else
    echo "prepend_path('PATH', '$homepath/bin')" >> module/Group_Python.lua
fi

rm -r bin
mkdir bin

ln -s $homepath/src/Numerical_integrator.py bin/
ln -s $homepath/src/data_properties.py bin/  
ln -s $homepath/src/exp_fit.py bin/       
ln -s $homepath/src/histogram.py bin/         
ln -s $homepath/src/interpolate.py bin/        
ln -s $homepath/src/polynomial_fit.py bin/

chmod 777 bin/*

source ~/.bash_profile
