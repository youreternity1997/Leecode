# 我使用了 python 預設的 sort() 語法來做到，不過在面試的時候，可能會不知道原來 python 的 sort() 可以滿足這樣的需求，但是這也沒有問題，因為 heap 的用法就是面試前一定要準備到的，也可以使用 heap 來重新去做到排序。
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()

        for i in range(1, len(intervals)):
            previous_begin_time, previous_end_time = intervals[i - 1]
            current_begin_time, current_end_time = intervals[i]
            if current_begin_time < previous_end_time:
                return False

        return True