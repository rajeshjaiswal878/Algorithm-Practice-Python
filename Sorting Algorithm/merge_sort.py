import time

'''
Hold Spot and Compare It With Other Value
'''


def merge_sort_recursive(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_recursive(left)
        merge_sort_recursive(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


'''def insertion_sort_iterative_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_iterative_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key'''

arr_passed = [64, 34, 25, 12, 22, 11, 90]

func_name = merge_sort_recursive.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
merge_sort_recursive(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
'''arr_passed1 = [64, 34, 25, 12, 22, 11, 90]
func_name = insertion_sort_iterative_recursive.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
insertion_sort_iterative_recursive(arr_passed1, len(arr_passed1))
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed1}')
print('-' * 20)'''
