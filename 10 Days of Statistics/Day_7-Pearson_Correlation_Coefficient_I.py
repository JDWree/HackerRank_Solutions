# Task:
# Given two 'n'-element data sets, 'X' and 'Y',
# calculate the value of the Pearson correlation coefficient.

n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

def mean(arr):
    """Calculates the mean of a 1D data set"""
    return sum(arr)/len(arr)

def std(arr):
    """Calculates the standard deviation of a 1D data set"""
    m = mean(arr)
    sqrd_sum = 0
    for i in range(len(arr)):
        sqrd_sum += (arr[i]-m)**2

    return (sqrd_sum/len(arr))**.5

def pcc(arr1, arr2):
    """Calculates the Pearson correlation coefficient"""
    m1 = mean(arr1)
    m2 = mean(arr2)
    std1 = std(arr1)
    std2 = std(arr2)

    n = len(arr1)

    p_sum = 0
    for i in range(n):
        p_sum += (arr1[i] - m1) * (arr2[i] - m2)

    return p_sum/(n*std1*std2)

print(f"{pcc(X,Y):.3f}")
