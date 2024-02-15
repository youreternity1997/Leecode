# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:34:25 2021

@author: User
"""

List = [2,4,6,8,11]
target = 13
Dict = {}

for i in range(len(List)):
    diff = target - List[i]
    if diff in Dict:
        print([Dict[target-List[i]], i])
        #return [Dict[target-List[i]], i]
    
    else:
        Dict[List[i]] = i
        

