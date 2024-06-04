"""Sorted Squared Array - You are given an array of Integers in which each 
subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares 
of each number sorted in ascending order."""


def sorted_array(arr):
    square_array = [x*x for x in arr]
    square_array.sort()
    return square_array


print(sorted_array([1, 2, 3, 4, 5]))
