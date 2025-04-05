# https://leetcode.com/problems/merge-two-sorted-lists/solutions/6045399/0-ms-runtime-beats-100-user-step-by-steps-solution-easy-to-understand/
# Time Complexity: O(m + n), where (m) and (n) are the lengths of list1 and list2
# Space Complexity: O(1), as we only use pointers and no additional space beyond the merged list.
# Beats 100%

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)   # 建立一個虛擬節點，幫助簡化串接的過程
        current = dummy       # current 是我們操作的游標

        # 當 list1 和 list2 都還沒跑完時，持續比較每個節點
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1     # 把較小的節點接到 current 後面
                list1 = list1.next       # 然後 list1 往後移動一格
            else:
                current.next = list2     # 同理
                list2 = list2.next
            current = current.next       # current 自己也往後移動一格

        # 有一個串列跑完後，把另一個剩下的全部接上去
        current.next = list1 if list1 else list2

        return dummy.next  # 回傳真正的頭節點（dummy.next）
