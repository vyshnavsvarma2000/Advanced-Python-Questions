def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
     # Compute the sum of the first window
    max_sum = sum(arr[:k])
    current_sum = max_sum
    # Slide the window from start to end of the array
    for i in range(n-k):
        current_sum = current_sum - arr[i] + arr[i+k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


print(max_sum_subarray([2,1,5,5,3,2],3))