class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # 會議室是空的
        heap = []

        # 使用了一間會議室，記錄他們的「結束」時間
        heapq.heappush(heap, intervals[0][1])    
        count = 1

        for i in range(1, len(intervals)):
            # 要來使用會議室的人
            interval = intervals[i]

            # 在所有會議室的結束時間，最早的結束時間有沒有比現在要開會的人的時間還早的？
            if interval[0] >= heap[0]:
                # 有喔，所以我們可以把那組人的時間結束時間給刪掉了
                # 這組人就可以開始使用這個空間
                heapq.heappop(heap)  
            else:
                # 沒有喔，所以目前沒有會議室可以用了，加開一間使用
                count += 1

            # 這組人開始使用會議室了，記錄「結束」時間
            heapq.heappush(heap, interval[1])
        return count