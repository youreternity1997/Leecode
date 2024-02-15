# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 02:44:27 2021

@author: User
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        else:
            string = str(x)
            Len = len(string)
            H_len = Len//2
         
            for i in range(H_len):
                if string[i] != string[-(i+1)]:
                    return False
                else:
                    pass
        
            return True


Solution().isPalindrome(121)