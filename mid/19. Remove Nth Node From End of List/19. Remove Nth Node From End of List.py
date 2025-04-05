# https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/4813340/beat-100-00-full-explanation-with-pictures/
# 時間複雜度：O(n)
# 空間複雜度：O(1)
# Beats 100%

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)        # 建立一個虛擬節點 dummy，並連接到 head
        dummy.next = head
        first = dummy              # first 指針，初始位置 dummy
        second = dummy             # second 指針，也在 dummy

        for _ in range(n + 1):     # 先讓 first 前進 n+1 步
            first = first.next

        while first is not None:   # 然後 first 和 second 一起前進，直到 first 到尾端
            first = first.next
            second = second.next

        # 此時 second 正好在要刪除的節點前一個
        second.next = second.next.next  # 刪除目標節點

        return dummy.next          # 回傳新的 head（即 dummy.next）
        second.next = second.next.next

        return dummy.next