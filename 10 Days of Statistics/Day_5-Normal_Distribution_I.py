# Task
# In a certain plant, the time taken to assemble a car is a random variable, ,
# having a normal distribution with a mean of 'm' hours
# and a standard deviation of 's' hours.
# What is the probability that a car can be assembled at this plant in:
#
#   1. Less than 'q1' hours?
#   2. Between 'q2_l' and 'q2_h' hours?


m, s = list(map(float, input().rstrip().split()))
q1 = float(input())
q2_l, q2_h = list(map(float, input().rstrip().split()))

def ND_cumul_func(m,s,x):
    """Calculates the cumulative probability of X <= 'x'
    where X follows a normal distribution with mean 'm'
    and standard deviation 's'."""
    #from scipy.special import erf
    import math
    z = (x-m)/(s*math.sqrt(2))
    return .5*(1+math.erf(z))

print(f"{ND_cumul_func(m,s,q1):.3f}")
print(f"{ND_cumul_func(m,s,q2_h)-ND_cumul_func(m,s,q2_l):.3f}")
