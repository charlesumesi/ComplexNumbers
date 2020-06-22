# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import cmath

def invert_complex():
    x = float(input('Enter the real part of your complex number : '))
    y = float(input('Enter the imaginary part of your complex number : '))
    return complex(x,-y)/(x**2 + y**2)

print(invert_complex())