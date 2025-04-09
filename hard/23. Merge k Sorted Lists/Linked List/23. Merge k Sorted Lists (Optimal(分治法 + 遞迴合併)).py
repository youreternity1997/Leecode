# https://leetcode.com/problems/merge-k-sorted-lists/solutions/6124518/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Time complexity : O(N log k) N 是所有節點的總數，k 是串列數量。每層合併花 O(N)，共有 log k 層（每次把 k 個串列減半）
# Space complexity : O(n) 最差為 O(log k)：來自遞迴堆疊。如果你使用的是遞迴合併函數（如 mergeTwoLists()），則也會消耗最多 O(n) 的堆疊記憶體
# Beats 99%

from typing import List, Optional
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divideAndConquer(lists, 0, len(lists) - 1)

    def divideAndConquer(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]

        mid = left + (right - left) // 2
        l1 = self.divideAndConquer(lists, left, mid)
        l2 = self.divideAndConquer(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)