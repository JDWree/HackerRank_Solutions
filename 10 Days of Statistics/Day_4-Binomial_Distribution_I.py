t, d = input().rstrip().split()
t, d = float(t), float(d)
p = t/(t+d)
q = 1 - p
n = 6
x = 3 # AT LEAST 3 boys

def fact(x):
    """Returns the factorial of x (x!)."""
    return 1 if x == 0 else x*fact(x-1)

def combination(n,r):
    """Returns the combinations of r samples out of n objects."""
    return fact(n)/(fact(r)*fact(n-r))

def binomial(r,n,p):
    """Calculates the binomial probability of r successes out of n trials
    with a probability p for a success."""
    return combination(n,r) * p**r * (1-p)**(n-r)

result = sum(binomial(i,n,p) for i in range(x, n+1))
print(f"{result:.3f}")
