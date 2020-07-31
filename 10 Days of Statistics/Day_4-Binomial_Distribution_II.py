# No more than 2 rejects: sum(0,1 and 2 rejects out of 10)
# At least 2 rejects: sum(2,3,...,10 rejects out of 10)

P, n = list(map(int, input().rstrip().split()))
p = P/100

def fact(x):
    """Calculates the factorial of 'x' (x!)."""
    return 1 if x == 0 else x*fact(x-1)

def comb(x,n):
    """Returns the  unorderd combinations of 'x' out of 'n' samples."""
    return fact(n)/(fact(x)*fact(n-x))

def b(x,n,p):
    """Calculates the binomial probability of 'x' successes out of 'n' trials
    with probability 'p' for a success."""
    return comb(x,n) * p**x * (1-p)**(n-x)

print(f"{sum(b(i,n,p) for i in range(0,3)):.3f}")
print(f"{sum(b(i,n,p) for i in range(2,11)):.3f}")
