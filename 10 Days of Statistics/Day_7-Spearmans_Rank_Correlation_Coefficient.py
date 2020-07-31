# Task:
# Given two 'n'-element data sets, 'X' and 'Y',
# calculate the value of Spearman's rank correlation coefficient.

n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

def mean(arr):
    """Calculate the mean of a 1D data set"""
    return sum(arr)/len(arr)

def std(arr):
    """Calcuate the standard deviation of a 1D data set"""
    m = mean(arr)
    s_sum = 0
    for i in arr:
        s_sum += (i-m)**2

    return (s_sum/len(arr))**.5

def cov(arr1, arr2):
    """Calcuate the covariance between two 1D data sets of equal length."""
    m1 = mean(arr1)
    m2 = mean(arr2)
    cov_sum = 0
    for i,j in zip(arr1, arr2):
        cov_sum += (i-m1)*(j-m2)

    return cov_sum/len(arr1)

def pcc(arr1, arr2):
    """Calculates the Pearson correlation coefficient between two 1D data sets."""
    std1 = std(arr1)
    std2 = std(arr2)
    cova = cov(arr1, arr2)

    return cova/std1/std2

def rank(arr):
    """Creates a ranking array for given 1d data set"""
    rank_dic = dict(zip(sorted(set(arr)),
    [i for i in range(1,len(set(arr))+1)]))

    rank_array = []
    for i in arr:
        rank_array.append(rank_dic[i])

    return rank_array

def srcc(arr1, arr2):
    """Calculate the Spearman's rank correlation coefficient of two 1D data sets"""
    rank1 = rank(arr1)
    rank2 = rank(arr2)

    if len(X) == len(set(X)) and len(Y) == len(set(Y)):
        n = len(arr1)
        d = 0
        for i,j in zip(rank1, rank2):
            d += (i-j)**2

        return 1 - (6 * d / (n * (n**2 - 1)))

    else:
        return pcc(rank1,rank2)


print(f"{srcc(X,Y):.3f}")
