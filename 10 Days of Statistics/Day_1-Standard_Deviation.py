_ = input()
X = list(map(int, input().rstrip().split()))

def mean(arr):
    "Calculates the mean of a 1D data set."
    return sum(arr)/len(arr)

def stdv(arr):
    "Calculates the standard deviation of a 1D data set."
    sqrd_sum = 0
    m = mean(arr)
    for i in range(len(arr)):
        sqrd_sum += (arr[i] - m)**2.
    from math import sqrt
    return sqrt(sqrd_sum/len(arr))



print(f"{stdv(X):.1f}")
