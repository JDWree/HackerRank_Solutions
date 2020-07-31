# Task:
# A large elevator can transport a maximum of 'max_load' pounds.
# Suppose a load of cargo containing 'n' boxes must be transported
# via the elevator. The box weight of this type of cargo follows a distribution
# with a mean of 'mean' pounds and a standard deviation of 'std' pounds.
# Based on this information, what is the probability that all 'n' boxes can be
# safely loaded into the freight elevator and transported?

max_load = int(input())
n = int(input())
mean = float(input())
std = float(input())

def nd(x,mean, std):
    """Calculates the probability of X = 'x' where X has a normal distribution
    with 'mean' and standard deviation 'std'."""
    import math
    return (1/(std*math.sqrt(2)))*math.exp((-.5)*(x-mean)**2 / std**2)

def cdf(x,mean ,std):
    """Calculates the cumulative probability of X <= 'x'
    where X has a normal distribution with 'mean' and standard deviation 'std'."""
    import math
    z = (x-mean)/(std*math.sqrt(2))
    return .5*(1+math.erf(z))

print(f"{cdf(max_load, n*mean, n**.5*std):.4f}")
