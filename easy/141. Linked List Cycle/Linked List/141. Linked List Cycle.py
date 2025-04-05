# https://leetcode.com/problems/linked-list-cycle/solutions/6556606/0ms-100-step-by-step-explained-with-visualization-easiest-to-understand-java-c-python/
# 使用「快慢指針」法（又叫佛洛伊德循環檢測演算法，Floyd’s Cycle-Finding Algorithm）
# Time complexity:O(n) 最多遍歷整個鏈結串列一次
# Space complexity: O(1) 只用了兩個指針（無額外空間）
# Beats 100%

class Solution(object):
    def hasCycle(self, head):
        slow = head  # 慢指針
        fast = head  # 快指針

        # 當快指針和其下一個節點不為空時繼續循環
        while fast is not None and fast.next is not None:
            slow = slow.next          # 慢指針走一步
            fast = fast.next.next     # 快指針走兩步

            if slow == fast:          # 如果兩個指針相遇，代表有環
                return True

        return False  # 若快指針走到底了，代表無環
