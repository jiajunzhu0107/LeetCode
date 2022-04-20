# https://leetcode.com/problems/trapping-rain-water/
#this is brute force
# DP, stack, Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        left = None
        #open = True # -1 to indicate still open
        lake = []
        res = 0
        for i, h in enumerate(height):
            if i == 0:
                continue
            if len(lake) <= 0:
                if h < height[i-1]:	   
                    if len(lake) == 0:
                        left = height[i-1]
                        lake = [height[i-1],h]
                else:
                    continue
            else:
                if h <= height[i-1]:	  
                    lake.append(h)
                else: #h > height[i-1]
                    if h >= left: #closed a lake
                        lake_surface = left
                        res += sum([lake_surface - lake[i] for i in range(1,len(lake))])
                        left = h
                        lake = []
                    else: #formed a lake, but still open for expansion
                        lake.append(h)
        # print(res)
        if len(lake) > 0: #calculate the open lake
            left_index = 0
            for i in range(1, len(lake)): #left is the highest so far
                if lake[i] > lake[i-1] and i > left_index:
                    # print(i)
                    heighest_peak = max(lake[i:])
                    # print(heighest_peak)
                    heighest_peak_ind = lake[i:].index(heighest_peak) + i
                    # print(heighest_peak_ind)

                    lake_surface = heighest_peak
                    # print(lake)
                    # print(left_index+1, heighest_peak_ind)
                    res += sum([lake_surface - lake[j] if (lake_surface - lake[j]) > 0 else 0 for j in range(left_index+1, heighest_peak_ind )] )
                    # print(res)
                    left_index = heighest_peak_ind 
			
			
				
        return res
        