N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

def mean(arr):
    """Calculates the mean of a 1D data set."""
    return sum(arr)/len(arr)


def median(arr):
    """Calculates the median of a 1D data set."""
    from math import floor, ceil
    sarr = sorted(arr)

    if len(arr)%2 == 0:
        #print(sarr, sarr[int(len(arr)/2-1)], sarr[int(len(arr)/2)])
        return (sarr[int(len(arr)/2-1)]+sarr[int(len(arr)/2)])/2.
    else:
        return sarr[ceil(len(arr)/2)]


def mode(arr):
    """Returns the mode of a 1D data set.
    If the data set is multimodal, returns the numerical smallest one."""
    # Creating a dictionary with occurrences.
    # Sort it first by key (data) then by value (occurrence).
    occs = {key: arr.count(key) for key in set(arr)}
    sbk_occs = {k:v for k,v in sorted(occs.items(), key = lambda item: item[0])}
    sbv_occs = {k:v for k,v in sorted(sbk_occs.items(), key = lambda item: item[1],
    reverse = True)}

    return next(iter(sbv_occs.items()))[0]

print(f"{mean(arr):.1f}")
print(f"{median(arr)}")
print(mode(arr))
