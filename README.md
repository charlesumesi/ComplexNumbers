# ComplexNumbers
A Python code that can multiply an infinite number of complex numbers using the input command
```python
import cmath

def multiply_complex():
   
    # Compile one list of all numbers and complex numbers to be multiplied
    a = int(input('How many numbers and complex numbers are you multiplying? : '))
    b = "Enter one real and its corresponding imaginary part in the format R,I\n(for absent real or imaginary part, enter '0', as in R,0 or 0,I) : "
    c = [list(input(b)) for _ in [0]*a]
    ...
```
