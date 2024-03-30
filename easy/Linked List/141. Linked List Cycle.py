# https://leetcode.com/problems/linked-list-cycle/
# Time complexity:0(n)
# Space complexity:0(1)

class Solution:
    def hasCycle(self, head):
        if not head or not head.next: # Empty or One Node
            return False
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
                
        return False