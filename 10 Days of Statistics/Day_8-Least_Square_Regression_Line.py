# Task:
# A group of five students enrolls in Statistics immediately
# after taking a Math aptitude test.
# Each student's Math aptitude test score, x, and Statistics course grade, y,
# can be expressed as the following list of  points:
#   1. (95,85)
#   2. (85, 95)
#   3. (80, 70)
#   4. (70, 65)
#   5. (60,70)
#
# If a student scored an '80' on the Math aptitude test,
# what grade would we expect them to achieve in Statistics?
# Determine the equation of the best-fit line using the least squares method,
# then compute and print the value of y when x = 80.

X,Y = [],[]
import sys
for i in sys.stdin.readlines():
    line = list(map(int, i.rstrip().split()))
    X.append(line[0])
    Y.append(line[1])

def mean(arr):
    """Calculates the mean of a 1D data set."""
    return sum(arr)/len(arr)

def std(arr):
    """Calculates the standard deviation of a 1D data set."""
    m = mean(arr)
    return ((sum([(i-m)**2 for i in arr])/len(arr))**.5)

def cov(arr1, arr2):
    """Calcuate the covariance between two 1D data sets of equal length."""
    m1 = mean(arr1)
    m2 = mean(arr2)

    return (sum([(i-m1)*(j-m2) for i,j in zip(arr1, arr2)])/len(arr1))

def pcc(arr1, arr2):
    """Calculates the Pearson correlation coefficient between two 1D data sets."""
    std1 = std(arr1)
    std2 = std(arr2)
    cova = cov(arr1, arr2)

    return cova/std1/std2

def reg_line(arr1, arr2):
    """Calculates the coefficients 'a' and 'b' of the linear regression line
    Y^ = a + b*X between two 1D data sets Y and X."""
    mx = mean(arr1)
    my = mean(arr2)

    stdx = std(arr1)
    stdy = std(arr2)

    r = pcc(arr1, arr2)

    b = r*stdy/stdx
    a = my - b * mx

    return (a,b)

a,b = reg_line(X,Y)
print(f"{a+b*80:.3f}")
