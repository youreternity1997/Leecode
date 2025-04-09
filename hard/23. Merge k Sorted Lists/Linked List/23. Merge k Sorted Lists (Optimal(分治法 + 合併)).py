# https://leetcode.com/problems/merge-k-sorted-lists/solutions/6156836/divide-and-conquer-method-beats-91-36/
# Time complexity : O(N log k) N 是所有節點的總數，k 是串列數量。每層合併花 O(N)，共有 log k 層（每次把 k 個串列減半）
# Space complexity : O(n) 最差為 O(log k)：來自遞迴堆疊。如果你使用的是遞迴合併函數（如 mergeTwoLists()），則也會消耗最多 O(n) 的堆疊記憶體
# Beats 99%

class Solution:
    def merge(self, head1, head2):
        new = ListNode()
        tmp = new
        while head1 and head2:
            if head1.val < head2.val:
                tmp.next = head1
                tmp = tmp.next
                head1 = head1.next
            else:
                tmp.next = head2
                tmp = tmp.next
                head2 = head2.next
        
        if head1:
            tmp.next = head1
        if head2:
            tmp.next = head2
        
        return new.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def devide(l, r):
            if l == r:
                return lists[l]

            elif l < r:
                mid = l + (r - l) // 2
                left = devide(l, mid)
                right = devide(mid + 1, r)
                new = self.merge(left, right)
                return new 
            else:
                return None

        return devide(0, len(lists) - 1)