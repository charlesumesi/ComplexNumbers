# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import cmath

def multiply_complex():
    '''Multiplies an infinite number of complex numbers'''
    
    # Compile one list of all numbers and complex numbers to be multiplied
    a = int(input('How many numbers and complex numbers are you multiplying? : '))
    b = "Enter one real and its corresponding imaginary part in the format R,I\n(for absent real or imaginary part, enter '0', as in R,0 or 0,I) : "
    c = [list(input(b)) for _ in [0]*a]
    
    # Tidy the list by converting to string and reconverting back to a list
    d = []
    for i in c:
        e = ''.join(i)
        d.append(e)
    
    # Use concatenation to convert each item in the list to string complex
    f = []
    for i in d:
        g = 'complex(' + i + ')'
        f.append(g)
    del(c, d)
    
    # Convert the edited list to string proper and evaluate
    return eval('*'.join(f))

print(multiply_complex())