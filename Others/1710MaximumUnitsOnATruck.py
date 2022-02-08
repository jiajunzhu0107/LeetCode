# https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxes = [[units,boxes] for boxes,units in boxTypes]
        sortedBoxes.sort(reverse = True)
        totalUnits = 0
        leftTruckSize = truckSize
        for units,boxes in sortedBoxes:
            loads = min(boxes,leftTruckSize)
            leftTruckSize -= loads
            totalUnits += units * loads
        return totalUnits