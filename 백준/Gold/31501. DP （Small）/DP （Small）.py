def binary_search_insert_position(arr, value, increasing=True):
    """
    Performs a binary search to find the insert position for `value` in `arr`.
    If `increasing` is True, it finds the position in an increasing sequence,
    otherwise in a decreasing sequence.
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if (increasing and arr[mid] < value) or (not increasing and arr[mid] > value):
            lo = mid + 1
        else:
            hi = mid
    return lo
 
 
n, q = map(int, input().split())
v = list(map(int, input().split()))
 
L, R, D = [0] * n, [0] * n, []
 
# Find LIS ending at each element
for i in range(n):
    t = binary_search_insert_position(D, v[i], True)
    if t == len(D):
        D.append(v[i])
    else:
        D[t] = v[i]
    L[i] = t + 1
 
D.clear()
 
# Find LDS starting from each element
for i in range(n - 1, -1, -1):
    t = binary_search_insert_position(D, v[i], False)
    if t == len(D):
        D.append(v[i])
    else:
        D[t] = v[i]
    R[i] = t + 1
 
# Combine LIS and LDS lengths
A = [int(input()) - 1 for _ in range(q)]
for i in A:
    print(L[i] + R[i] - 1)
