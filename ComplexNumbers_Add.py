# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import cmath

def add_complex():
    '''Adds an infinite number of complex numbers'''

    # Compile separate lists for real and imaginary parts
    x = list(map(float, (input('Enter comma separated real parts of your complex numbers : ')).split(',')))
    y = list(map(float, (input('Enter comma separated imaginary parts of your complex numbers : ')).split(',')))

    if float(sum(x)) == int(sum(x)) and float(sum(y)) == int(sum(y)):
        return complex(int(sum(x)), int(sum(y)))
    else:
        return complex(float(sum(x)), float(sum(y)))

print(add_complex())