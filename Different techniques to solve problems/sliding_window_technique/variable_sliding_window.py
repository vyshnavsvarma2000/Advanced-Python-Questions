def sliding_window_variable_size(arr, target):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += arr[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1 )
            current_sum -= arr[left]
            left+=1
    return min_length if min_length != float('inf') else 0

arr = [2, 3, 2, 2, 4, 0]
target = 7
print(sliding_window_variable_size(arr, target)) 