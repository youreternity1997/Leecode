# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:17:56 2023

@author: youreternity1997
"""

# Selection sort in Python

def selectionSort(array, size):
   
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
            
            # select the minimum element in each loop
            if array[j] < array[min_idx]:
                min_idx = j
         
        # put min at the correct position
        (array[i], array[min_idx]) = (array[min_idx], array[i])


data = [-22, 13,-1, 42, 45, 0, 11, -9, 33]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)