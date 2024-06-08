def sliding_window_fixed_size(arr, k):
    n = len(arr)
    if n < k:
        return -1
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(n-k):
        current_sum = current_sum - arr[i] + arr[i+k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(sliding_window_fixed_size(arr, k))
