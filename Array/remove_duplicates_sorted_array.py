def remove_duplicates(arr):
    n = len(arr)
    pivot = 0
    if n == 0 or n == 1:
        return arr
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[pivot] = arr[i]
            pivot = pivot + 1
    arr[pivot] = arr[n-1]
    return arr[0:pivot+1]


print(remove_duplicates([1, 2, 2, 3, 3, 4, 5]))
