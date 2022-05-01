# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heappop(heap)
                heappush(heap, end)
            else:
                heappush(heap, end)
        return len(heap)
