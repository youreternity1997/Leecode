# https://leetcode.com/problems/reverse-linked-list/solutions/6550282/0ms-100-step-by-step-visualization-easiest-to-understand-java-c-python/
# Time complexity: O(n) (linear time).
# Space complexity:O(1) (constant space).
# Beats 100%

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward

        return prev  # prev is the new head of the reversed list