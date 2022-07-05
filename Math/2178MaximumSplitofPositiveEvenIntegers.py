# 2178. Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# 2: 2, 4: 4, 6:2,4, 8:2,6; 10:2,8;4,6  12:2,4,6
#2, 4, 6, 8, 10
#2, 6, 12, 20, 30
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        start = 2
        end = 2
        i = 1
        closest_sum = (start + end) * i / 2
        
        while closest_sum <= finalSum:
            end += 2
            i += 1
            closest_sum = (start + end) * i / 2
            
        output = [2 * j for j in range(1, i)]
        output[-1] = finalSum - (closest_sum - end) + output[-1]
    
        return output
        