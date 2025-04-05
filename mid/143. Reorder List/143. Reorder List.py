# https://leetcode.com/problems/reorder-list/solutions/6115927/beats-super-easy-beginners/
# Time complexity: O(n) (找中間：O(n); 反轉後半段：O(n); 合併：O(n))
# Space complexity: O(1) as the reordering is done in-place with no additional data structures.
# Beats 100%

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Disconnect the two halves
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2