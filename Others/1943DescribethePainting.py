# https://leetcode.com/problems/describe-the-painting/

#line sweep
# [[1,4,5],[4,7,7],[1,7,9]]: [[1,4,14],[4,7,16]]
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        colors = {} # {1:14, 4:2, 7:-16}
        output = [] # [[1,4,14], [4,7,16]]
        for start, end, color in segments:
            if start in colors:
                colors[start] += color
            else:
                colors[start] = color
            if end in colors:
                colors[end] -= color
            else:
                colors[end] = -color
        current_color = 0
        prev_point = 0
        # print(colors)
        for point in sorted(colors.keys()):
            if prev_point == 0:
                prev_point = point
                current_color = colors[point]
                continue
            if current_color != 0:
                output.append([prev_point, point, current_color])
            prev_point = point
            current_color += colors[point]
        return output

# time out
from heapq import heapify, heappush, heappop
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        heapify(segments)
        output = []
        while segments:
            prev_start, prev_end, prev_color = heappop(segments)
            if not segments:
                output.append([prev_start, prev_end, prev_color])
                break
            current_start, current_end, current_color = heappop(segments)
            if current_start >= prev_end:
                heappush(segments, [current_start, current_end, current_color])
                output.append([prev_start, prev_end, prev_color])
            else:
                if current_start > prev_start:
                    heappush(segments, [prev_start, current_start, prev_color])
                heappush(segments, [current_start, min(prev_end, current_end), prev_color + current_color])
                if prev_end < current_end:
                    heappush(segments, [prev_end, current_end, current_color])
                elif prev_end > current_end:
                    heappush(segments, [current_end, prev_end, prev_color])
            # print(segments)
        return output
        