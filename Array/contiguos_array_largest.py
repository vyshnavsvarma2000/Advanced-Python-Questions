"""
Write a program to find the largest sum of 3 contiguous elements of an array.
Expected Output:
The given array is: 8 3 8 -5 4 3 -4 3 5
The largest sum of the contiguous subarray is: 19
"""

def contiguous(arr):
    n = len(arr)
    if n < 3:
        raise ValueError("Array must have atleast three elements ")
    # Calculate the sum of the first three elements
    max_sum = sum(arr[:3])
    current_sum = max_sum
    # Slide the window over the array
    for i in range(3, n):
        # Update the current sum by subtracting the element that is sliding out of the window
        # and adding the new element that is entering the window
        current_sum = current_sum - arr[i-3] + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
# Test the function with the given array
arr = [8, 3, 8, -5, 4, 3, -4, 3, 5]
print("The given array is ", arr)
print("The largest sum of the contiguous subarray is ", contiguous(arr))
