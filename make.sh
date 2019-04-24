#!/bin/bash

homepath=$(pwd)

if [ grep -q "module use $homepath/module" ~/.bash_profile ]; then
    echo "module use already in bash profile"
else
    echo "module use $homepath/module" >> ~/.bash_profile
    source ~/.bash_profile
fi

sed -i -e "s@AAA@$homepath/bin@g" Group_Python.lua

rm -r bin
mkdir bin

ln -s $homepath/src/Numerical_integrator.py bin/
ln -s $homepath/src/data_properties.py bin/  
ln -s $homepath/src/exp_fit.py bin/       
ln -s $homepath/src/histogram.py bin/         
ln -s $homepath/src/interpolate.py bin/        
ln -s $homepath/src/polynomial_fit.py bin/

chmod 777 bin/*
