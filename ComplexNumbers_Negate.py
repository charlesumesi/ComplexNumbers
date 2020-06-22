# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import cmath

def negate_complex():
    x = float(input('Enter the real part of your complex number : '))
    y = float(input('Enter the imaginary part of your complex number : '))
    
    if float(x) == int(x) and float(y) == int(y): return -1*complex(int(x), int(y))
    else: return -1*complex(float(x), float(y))

print(negate_complex())