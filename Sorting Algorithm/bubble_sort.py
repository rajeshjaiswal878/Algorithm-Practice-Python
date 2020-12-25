import time
''' 
Important Logic:
Highest Element will Be At The End
'''

def bubble_sort_brute_force(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        count += 1
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'After {count} Iteration Output: {arr}')
    return arr


def bubble_sort_swapped(arr):
    flag = True
    count = 0
    n = len(arr)
    while flag:
        flag = False
        for j in range(n - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
            print(f'After {count} Iteration Output: {arr}')
    return arr


def bubble_sort_swapped_for(arr):
    flag = True
    count = 0
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(n - 1 - i):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
            print(f'After {count} Iteration Output: {arr}')
        if not flag:
            break
    return arr


'''def bubble_sort_recursive(arr, n):
    if n is None:
        return
    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return bubble_sort_recursive(arr[:n - 1], n - 1)'''

arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = bubble_sort_brute_force.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = bubble_sort_brute_force(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
func_name = bubble_sort_swapped.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = bubble_sort_swapped(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
func_name = bubble_sort_swapped_for.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = bubble_sort_swapped_for(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
'''func_name = bubble_sort_recursive.__name__
func_name = func_name.replace('_', ' ').title()
n_passed = len(arr_passed)
start = time.time()
result = bubble_sort_recursive(arr_passed, n_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)'''
