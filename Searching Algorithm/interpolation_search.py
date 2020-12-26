import time

''' 
This Search Used For Array Those Are Sorted & Uni-formly Distributed 
'''


def interpolation_search_recursive(arr, lo, hi, val):
    if lo <= hi and arr[lo] <= val <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (val - arr[lo]))
        if arr[pos] == val:
            return pos
        if arr[pos] < val:
            return interpolation_search_recursive(arr, pos + 1, hi, val)
        if arr[pos] > val:
            return interpolation_search_recursive(arr, lo, pos - 1, val)
    return -1


def interpolation_search_iterative(arr, lo, hi, val):
    while lo <= hi and arr[lo] <= val <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (val - arr[lo]))
        if arr[pos] == val:
            return pos
        if arr[pos] < val:
            lo = pos + 1
            # return interpolation_search_iterative(arr, pos + 1, hi, val)
        if arr[pos] > val:
            hi = pos - 1
            # return interpolation_search_iterative(arr, lo, pos - 1, val)
    return -1


arr_one = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
val_one = 21
tic = time.time()
res = interpolation_search_recursive(arr_one, 0, len(arr_one) - 1, val_one)
toc = time.time()
time_taken = toc - tic
print(f'Recursive Way Val: {val_one} Found At: {res} Index Took:{time_taken} time')

tic = time.time()
res = interpolation_search_iterative(arr_one, 0, len(arr_one) - 1, val_one)
toc = time.time()
time_taken = toc - tic
print(f'Iterative Way Val: {val_one} Found At: {res} Index Took:{time_taken} time')
