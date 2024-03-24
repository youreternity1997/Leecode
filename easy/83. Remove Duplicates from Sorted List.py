class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        if head is not None:
            while pointer.next is not None:
                if pointer.val == pointer.next.val:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
        return head