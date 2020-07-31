# Task:
# The final grades for a Physics exam taken by a large group of students
# have a mean of 'mean' and a standard deviation of 'std'.
# If we can approximate the distribution of these grades
# by a normal distribution, what percentage of the students:
#
#  1.Scored higher than  'grade1' (i.e., have a grade > 'grade1')?
#  2.Passed the test (i.e., have a grade >= 'grade2')?
#  3.Failed the test (i.e., have a grade < 'grade2')?
#
# Find and print the answer to each question on a new line,
# rounded to a scale of 2 decimal places.

mean, std = list(map(float, input().rstrip().split()))
grade1 = float(input())
grade2 = float(input())

def cdf(mean, std, x):
    """Calculates the cumulative probability of X <= 'x'
    where X follows a normal distribution with 'mean'
    and standard deviation 'std'."""
    import math
    z = (x-mean)/(std*2.**.5)
    return .5*(1+math.erf(z))

# > grade1
print(f"{(cdf(mean, std, 120.)-cdf(mean, std, grade1))*100:.2f}")
# > grade2
print(f"{(cdf(mean, std, 120.)-cdf(mean, std, grade2))*100:.2f}")
# < grade2
print(f"{(cdf(mean, std, grade2)-cdf(mean, std, 0.))*100:.2f}")
