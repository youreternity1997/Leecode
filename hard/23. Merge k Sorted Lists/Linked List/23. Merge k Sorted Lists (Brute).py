# https://leetcode.com/problems/merge-k-sorted-lists/solutions/3286803/python3-and-c-95-ms-beats-95-60-and-easy/
# Time complexity : O(N log N) 排序花費 O(N log N)
# Space complexity : O(n) 額外使用一個陣列 v 存所有值
# Beats 99.04%

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        v=[]
        for i in lists:
            x=i
            while x:
                v+=[x.val]
                x=x.next
        v=sorted(v,reverse=True)
        ans=None
        for i in v:
            ans=ListNode(i,ans)
        return ans