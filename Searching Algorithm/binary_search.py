import time

''' 
This Search Used For Array Those Are Sorted
'''


def binary_search_recursive(arr, lo, hi, val):
    if lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            return binary_search_recursive(arr, mid + 1, hi, val)
        if arr[mid] > val:
            return binary_search_recursive(arr, lo, mid - 1, val)
    return -1


def binary_search_iterative(arr, lo, hi, val):
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            lo = mid + 1
            # return binary_search_recursive(arr, mid + 1, hi, val)
        if arr[mid] > val:
            hi = mid - 1
            # return binary_search_recursive(arr, lo, mid - 1, val)
    return -1


arr_one = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
val_one = 23
tic = time.time()
res = binary_search_recursive(arr_one, 0, len(arr_one) - 1, val_one)
toc = time.time()
time_taken = toc - tic
print(f'Recursive Way Val: {val_one} Found At: {res} Index Took:{time_taken} time')

tic = time.time()
res = binary_search_iterative(arr_one, 0, len(arr_one) - 1, val_one)
toc = time.time()
time_taken = toc - tic
print(f'Iterative Way Val: {val_one} Found At: {res} Index Took:{time_taken} time')
