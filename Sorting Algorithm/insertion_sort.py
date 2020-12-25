import time

'''
Hold Spot and Compare It With Other Value
'''
count = 0


def insertion_sort_iterative_while(arr):
    count = 0
    n = len(arr)
    for i in range(1, n):
        count += 1
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'After {count} Iteration Output: {arr}')
    return arr


def insertion_sort_iterative_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_iterative_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


arr_passed = [64, 34, 25, 12, 22, 11, 90]

func_name = insertion_sort_iterative_while.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = insertion_sort_iterative_while(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
arr_passed1 = [64, 34, 25, 12, 22, 11, 90]
func_name = insertion_sort_iterative_recursive.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
insertion_sort_iterative_recursive(arr_passed1, len(arr_passed1))
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed1}')
print('-' * 20)
