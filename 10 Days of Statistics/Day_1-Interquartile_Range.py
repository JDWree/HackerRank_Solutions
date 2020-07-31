n = int(input().strip())
X = list(map(int, input().rstrip().split()))
F = list(map(int, input().rstrip().split()))

S = []
for i in range(n):
    S.extend([X[i]]*F[i])
S = sorted(S)

def median(arr):
    """Calculates the median of a 1D data set."""
    if len(arr)%2 == 0:
        return (arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])/2.
    else:
        return arr[int(len(arr)/2)]

def split_arr(arr):
    """Split the 1D data set into lower half and upper half parts."""
    if len(arr)%2 == 0:
        LH = arr[:int(len(arr)/2)]
        UH = arr[int(len(arr)/2):]
    else:
        LH = arr[:int(len(arr)/2)]
        UH = arr[int(len(arr)/2)+1:]
    return LH, UH

LH, UH = split_arr(S)
Q_diff = median(UH)-median(LH)
#print(len(S), S, '\n', LH, UH, f"{Q_diff:.1f}")
print(f"{Q_diff:.1f}")
