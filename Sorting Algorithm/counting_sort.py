import time


def counting_sort(arr):
    mx_el = max(arr)
    mn_el = min(arr)
    el_range = mx_el - mn_el + 1
    print(el_range)
    count_arr = [0 for _ in range(el_range)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i] - mn_el] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - mn_el] - 1] = arr[i]
        count_arr[arr[i] - mn_el] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]

    print('Count Array:', count_arr)
    print('Output Array:', output_arr)
    return arr


arr_passed = [64, 34, 25, 12, 22, 11, 90]
func_name = counting_sort.__name__
func_name = func_name.replace('_', ' ').title()
start = time.time()
result = counting_sort(arr_passed)
end = time.time()
print(f'*** {func_name} Took:{(end - start)} seconds to Sort, Final Output:{result}')
print('-' * 20)
