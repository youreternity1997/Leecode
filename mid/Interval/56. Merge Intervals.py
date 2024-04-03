# https://leetcode.com/problems/merge-intervals/solutions/3462073/ex-amazon-explains-a-solution-with-a-video-python-javascript-java-and-c/
# Time  complexity : O(nlogn) <= sorted()()nlogn) + for(n)
# Space complexity : O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x [0])
        print('intervals=', intervals)
        
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans