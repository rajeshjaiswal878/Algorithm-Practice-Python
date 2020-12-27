import time

'''
Hold Spot and Compare It With Other Value
'''


def partition_high(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition_low(arr, low, high):
    i = (low + 1)
    j = high
    pivot = arr[low]
    while i <= j:
        while arr[i] < pivot and i < j:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            i += 1
    arr[low] = arr[j]
    arr[j] = pivot
    return j

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition_low(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


arr_passed = [64, 34, 25, 12, 22, 11, 90]
low_passed = 0
high_passed = len(arr_passed) - 1
func_name = quick_sort.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
quick_sort(arr_passed, low_passed, high_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
