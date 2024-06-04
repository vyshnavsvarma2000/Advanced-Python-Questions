"""
 Monotonic Array - An array is monotonic if it is either monotone increasing or monotone decreasing. 
 An array is monotone increasing if all its elements from left to right are non-decreasing. 
 An array is monotone decreasing if all  its elements from left to right are non-increasing. 
 Given an integer array return true if the given array is monotonic, or false otherwise
"""


def is_monotonic(arr):
    if not arr:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            is_increasing = False

        if arr[i] > arr[i-1]:
            is_decreasing = False
    return is_decreasing or is_increasing


print(is_monotonic([3, 3, 2, 1]))
