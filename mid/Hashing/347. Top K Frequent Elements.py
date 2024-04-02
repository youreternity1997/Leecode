# https://leetcode.com/problems/top-k-frequent-elements/solutions/4580564/5-1-approach-1-o-n-log-n-python-c-step-by-step-explanation/
# Time complexity : O(n log n)
# Space complexity : O(n)
# Hash Map

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Use a dictionary (lis) to count the frequency of each element in nums.
        lis = {} 
        ans = [] 
        for x in nums:
            if x in lis:
                lis[x] += 1
            else:
                lis[x] = 1
        
        # Step 2: Sort the dictionary items based on frequency in descending order.
        slis = sorted(lis.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k frequent elements and append them to the ans list.
        for i in range(k):
            ans.append(slis[i][0])
        
        return ans