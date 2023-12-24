# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:33:07 2023

@author: User
"""

#Insertion Sort
data = [29, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 213, 92, 96, 96, 23]

def InsertionSort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i-1 
        # key < data[j]
        while j >=0 and key < data[j] :
            data[j+1] = data[j]
            j -= 1
            
        # key >= data[j]
        data[j+1] = key
    return data
        
print(InsertionSort(data))