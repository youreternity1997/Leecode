# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 03:02:52 2021

@author: User
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dct={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        return sum(dct[s[i]] if dct[s[i]]>=dct[s[i+1]] else -dct[s[i]] for i in range(len(s)-1))+dct[s[-1]]


Solution().romanToInt("MCMXCIV")aa
"M CM XC IV"
"M D C XC V"


