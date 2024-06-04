"""
Given an integer array nums, find the sum of the elements between
indices i and j (i<=j), inclusive
Example:
Given nums = [-2, 0, 3,-5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5)-> -1
sumRange(0, 5) -> -3
Note: You may assume that the array does not change
There are many calls to sumRange function
"""


class NumArray:
    def __init__(self, nums):
        # Initialize the prefix sum array with an extra initial 0 for ease of calculation
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        # The sum of elements between indices i and j is the difference
        # between the prefix sum at j+1 and the prefix sum at i
        return self.prefix_sums[j + 1] - self.prefix_sums[i]


# Example usage:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3
