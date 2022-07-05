# 2158. Amount of New Area Painted Each Day
#  https://leetcode.com/problems/amount-of-new-area-painted-each-day/

from heapq import heapify, heappush, heappop
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        points = {}
        for day, [start, end] in enumerate(paint):
            if start in points:
                points[start].append([day, 'start'])
            else:
                points[start] = [[day, 'start']]
            if end in points:
                points[end].append([day, 'end'])
            else:
                points[end] = [[day, 'end']]
        # print(points)
        current_days = []
        ended_days = {day:False for day in range(len(paint))}
        # ended_days = [False] * len(paint)
        # current_days = deque([])
        output = [0] * len(paint)
        for point in sorted(points.keys()):
            for day, status in points[point]:
                if status == 'start':
                    if current_days:
                        if day < current_days[0][0]:
                            output[current_days[0][0]] += point - current_days[0][1]
                    heappush(current_days, [day,point])
                else: #status == 'end'
                    # print(day, current_days[0])
                    if day > current_days[0][0]: # this day's work finished previously already
                        ended_days[day] = True
                    elif day == current_days[0][0]:
                        _, start = heappop(current_days)
                        output[day] += point - start
                        ended_days[day] = True
                        while current_days and ended_days[current_days[0][0]]:
                            heappop(current_days)
                        if current_days:
                            current_days[0][1] = point
                # print( ended_days, current_days, output)
                        
        return output
                                