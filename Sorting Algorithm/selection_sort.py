import time

'''
Hold Spot and Compare It With Other Value
'''


def selection_sort_iterative_for(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        count += 1
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print(f'After {count} Iteration Output: {arr}')
    return arr


def selection_sort_iterative_while(arr):
    count = 0
    spot = 0
    n = len(arr)
    while spot < n:
        count += 1
        for j in range(spot + 1, n):
            if arr[spot] > arr[j]:
                arr[spot], arr[j] = arr[j], arr[spot]
        spot += 1
        print(f'After {count} Iteration Output: {arr}')
    return arr


arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = selection_sort_iterative_for.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = selection_sort_iterative_for(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
func_name = selection_sort_iterative_while.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = selection_sort_iterative_while(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
