# Time complexity: O(n)
# Space complexity: O(1)
# Array + Hash Map

class Solution:
    def checkRecord(self, s: str) -> bool:
        total_absent = 0
        prev, late = '',  0
        for i in s:
            if i == 'A':
                total_absent += 1
                if total_absent >= 2:
                    return False
            elif i == 'L':
                if prev == 'L':
                    late += 1
                    if late >= 3:
                        return False
                else:
                    late = 1
            prev = i
        return True
        