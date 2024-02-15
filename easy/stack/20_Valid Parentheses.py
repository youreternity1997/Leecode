# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:33:56 2021

@author: User
"""

class Solution:
    def isValid(self, s: str) -> bool:
        match = {'{':'}', '(':')', '[':']'}
        stack = []
    
        for c in s:
            if c in match:
                stack.append(c)
            else:
                #print('stack=', stack)
                #print("stack.pop()=", stack.pop())
                #print('match[stack.pop()]=', match[stack.pop(-1)])
                #print('c=', c)
                if not stack or match[stack.pop()] != c:
                    return False

        return not stack
                
       

#s = "{()}"
#s = "{}()[]"

s = "[{()}]"
print(Solution().isValid(s))
