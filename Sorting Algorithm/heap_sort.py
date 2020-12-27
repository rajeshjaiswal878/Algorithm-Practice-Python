import time


def heapify(arr, n, last):
    key = last
    l = 2 * last + 1
    r = 2 * last + 2

    if l < n and arr[key] < arr[l]:
        key = l
    if r < n and arr[key] < arr[r]:
        key = r

    if key != last:
        arr[last], arr[key] = arr[key], arr[last]
        heapify(arr, n, key)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        # print('MaxHeap Build:', arr)
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # print('Extract:', arr)
        heapify(arr, i, 0)


arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = heap_sort.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
heap_sort(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
