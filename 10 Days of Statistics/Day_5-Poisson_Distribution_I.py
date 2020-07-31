# Task
# A random variable, 'X', follows Poisson distribution with mean of 'm'.
# Find the probability with which the random variable 'X' is equal to 'x'.

m = float(input())
x = float(input())

def fact(x):
    """Calculates the factorial of 'x' (x!)."""
    return 1 if x == 0 else x*fact(x-1)

import math

print(f"{math.exp(-m) * m**x / fact(x):.3f}")
