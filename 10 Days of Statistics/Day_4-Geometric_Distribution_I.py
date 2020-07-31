n, d = list(map(int, input().rstrip().split()))
p = n/d
n = int(input())

print(f"{(1-p)**4 * p:.3f}")
