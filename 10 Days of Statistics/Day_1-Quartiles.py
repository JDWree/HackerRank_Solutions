n = input()
arr = sorted(list(map(int, input().rstrip().split())))

def median(arr):
    """Calculates the median of a 1D array."""
    from math import ceil
    if len(arr)%2 == 0:
        return int((arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])/2)
    else: return arr[ceil(len(arr)/2)-1]

def split_arr(arr):
    """Split the array in the 3 parts to calculate the quartiles from."""
    if len(arr)%2 == 0:
        LH = arr[:int(len(arr)/2)]
        X = arr[int(len(arr)/2-1):int(len(arr)/2+1)]
        UH = arr[int(len(arr)/2):]
    else:
        from math import ceil
        LH = arr[:ceil(len(arr)/2)-1]
        X = [arr[ceil(len(arr)/2)-1]]
        UH = arr[ceil(len(arr)/2):]
    return LH, X, UH

LH, X, UH = split_arr(arr)
print(median(LH))
print(median(X))
print(median(UH))
