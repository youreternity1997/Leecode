# Recursion

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        next = head.next # next 指向第二個點
        head.next = self.swapPairs(next.next) # head 指向第三個點
        next.next = head # next.next 指向第一個點
        return next