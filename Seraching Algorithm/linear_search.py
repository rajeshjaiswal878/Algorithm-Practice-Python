import time

''' 
This Search Used For Array Those Are Not Sorted
'''


def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


arr_one = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
val_one = 21
tic = time.time()
res = linear_search(arr_one, val_one)
toc = time.time()
time_taken = toc - tic
print(f'Linear Way Val: {val_one} Found At: {res} Index Took:{time_taken} time')
