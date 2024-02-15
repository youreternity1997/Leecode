# 迭代
# while

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev = head
        cur  = head.next

        while prev and cur:
            # 「兩兩節點的數值交換」
            temp = prev.val;
            prev.val = cur.val;
            cur.val = temp;

            if not cur.next or not cur.next.next:
                break

            # 「兩兩節點的鏈結」
            prev = cur.next;
            cur  = cur.next.next;     
        
        return head