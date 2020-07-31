# Task
# The manager of a industrial plant is planning to buy a machine
# of either type 'A' or type 'B' . For each day’s operation:

# The number of repairs, 'X', that machine 'A' needs is a Poisson random variable
# with mean 'mA'. The daily cost of operating 'A' is 'CA = 160 + 40*X**2'.
# The number of repairs, 'Y', that machine 'B' needs is a Poisson random variable
# with mean 'mB'. The daily cost of operating 'B' is 'CB = 128 + 40*Y**2'.

# Assume that the repairs take a negligible amount of time
# and the machines are maintained nightly to ensure that they operate like new
# at the start of each day.
# Find and print the expected daily cost for each machine.

mA, mB = list(map(float, input().rstrip().split()))

def fact(x):
    """Calculates the factorial of 'x' (x!)."""
    return 1 if x == 0 else x*fact(x-1)

def poisson(m,x):
    "Calculates the Poisson probability of 'x' with mean 'm'."
    import math
    return m**x * math.exp(-m) / fact(x)

# X**2 = mA + mA**2

print(f"{160+40*(mA + mA**2):.3f}")
print(f"{128+40*(mB + mB**2):.3f}")
