def max_sum_sub_array(arr):
    n = len(arr)
    st = 0
    end = 0
    poi = 0
    current_sum = 0
    max_sum = arr[0]

    for i in range(n):
        current_sum = current_sum + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            st = poi
            end = i
        if current_sum < 0:
            current_sum = 0
            poi = i+1
    print("Start index is", st)
    print("End index is ", end)
    print("Max sum subarray is ", max_sum)


max_sum_sub_array([4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1])
