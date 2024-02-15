# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:17:24 2021

@author: User
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        str_list = [string for string in strs]
        min_len = min([len(string) for string in str_list])
        
        if min_len == 0:
            empty = ""
            return empty
        elif len(str_list) == 1:
            return str_list[0]
        
        ans = ""
        for i in range(min_len):
            for j in range(len(strs)-1):
            
                if strs[j][i] == strs[j+1][i]:
                    pass
                else:
                    print('ans=', ans)
                    return ans
                
            ans += strs[0][i]
        return ans
    
strs = ['ab', 'a']
Solution().longestCommonPrefix(strs)