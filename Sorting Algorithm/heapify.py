import heapq
import time


def heapify_process(arr, n, last):
    print(arr)
    key = last
    l = 2 * last + 1
    r = 2 * last + 2
    if l < n and arr[key] < arr[l]:
        key = l
    if r < n and arr[key] < arr[r]:
        key = r
    if key != last:
        arr[last], arr[key] = arr[key], arr[last]
        heapify_process(arr, n, key)


def heapify_package(arr):
    heapq.heapify(arr)


arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = heapify_process.__name__
func_name = func_name.replace('_', ' ').title()
n = len(arr_passed)
start = time.time()
heapify_process(arr_passed, n, n - 1)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = heapify_package.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
heapify_package(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
