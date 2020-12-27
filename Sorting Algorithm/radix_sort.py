import time


def counting_sort(arr, exp):
    n = len(arr)
    output_arr = [0] * n
    count_arr = [0] * 10

    for i in range(n):
        index = (arr[i] / exp)
        count_arr[int(index % 10)] += 1
    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] / exp)
        output_arr[count_arr[int(index % 10)] - 1] = arr[i]
        count_arr[int(index % 10)] -= 1
    for i in range(n):
        arr[i] = output_arr[i]


def radix_sort(arr):
    mx_el = max(arr)
    exp = 1
    while (mx_el / exp) > 0:
        counting_sort(arr, exp)
        exp *= 10


arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = radix_sort.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
radix_sort(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{arr_passed}')
print('-' * 20)
