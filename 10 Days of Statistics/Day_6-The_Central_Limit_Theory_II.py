# Task:
# The number of tickets purchased by each student for
# the University X vs. University Y football game follows a distribution
# that has a mean of 'mean' and a standard deviation of 'std'.

# A few hours before the game starts, 'students' eager students line up
# to purchase last-minute tickets. If there are only 'tickets' tickets left,
# what is the probability that all students will be able to purchase tickets?

tickets = int(input())
students = int(input())
mean = float(input())
std = float(input())

import math

def cdf(x, mean, std):
  """Calculates the cumulative probability of X <= 'x'
  where X has a normal distribution with 'mean' and standard deviation 'std'."""
    z = (x-mean)/(std*2**.5)
    return .5*(1+math.erf(z))

print(f"{cdf(tickets, students*mean, math.sqrt(students)*std):.4f}")
