# -*- coding: utf-8 -*-
# Binary Search in python

def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")