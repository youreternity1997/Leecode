# https://leetcode.com/problems/non-overlapping-intervals/solutions/3785409/beat-s-100-c-java-python-beginner-friendly/
# Greedy
# Time complexity : O(nlogn)
# Space complexity : O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count