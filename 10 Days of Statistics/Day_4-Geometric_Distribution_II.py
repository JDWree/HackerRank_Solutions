# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the  defect is found during the first 5 inspections?

n, d = list(map(int, input().rstrip().split()))
p = n/d
n = int(input())

def fact(x):
    """Calculates the factorial of 'x' (x!)."""
    return 1 if x == 0 else x*fact(x-1)

def combi(r,n):
    """Returns the unorderd combinations of 'r' out of 'n' samples."""
    return (fact(n)/(fact(r)*fact(n-r)))

def neg_bi(r,n,p):
    """Calculates the negative binomial probability of  'r' successes out of 'n' trials
    with a probability 'p' for a success."""
    return combi(r-1,n-1) * p**r *(1-p)**(n-r)

# Geometric distribution probability for first success on 1st, 2nd,... or 5th trial.
print(f"{sum(p*(1-p)**(i-1) for i in range(1,6)):.3f}")
