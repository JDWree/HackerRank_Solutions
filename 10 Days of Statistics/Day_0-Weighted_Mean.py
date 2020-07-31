_ = input()
X = list(map(int, input().rstrip().split()))
W = list(map(int, input().rstrip().split()))

def product(x,y):
    """Creates a list of products between respective elements
     of two 1D data sets."""
    try:
        z = []
        for i in range(len(x)):
            z.append(x[i]*y[i])
        return z
    except IndexError:
        return None

try:
    w_mean = sum(product(X,W))/sum(W)
    print(f"{w_mean:.1f}")
except TypeError:
    print("Error!")
    print("The data set and its respective weights are not of the same length!")
