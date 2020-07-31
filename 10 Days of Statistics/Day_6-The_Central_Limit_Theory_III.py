# Task:
# You have a sample of 'n' values from a population with mean 'mean'
# and with standard deviation 'std'. Compute the interval that covers
# the middle 'interval' of the distribution of the sample mean; in other words,
# compute A and B such that P(A < x < B) = 'interval'.
# Use the value of 'z'. Note that 'z' is the z-score.


n = int(input())
mean = float(input())
std = float(input())
interval = float(input())
z = float(input())

import math

print(f"{(n * mean - z * n**.5 * std)/100:.2f}")
print(f"{(n * mean + z * n**.5 * std)/100:.2f}")
