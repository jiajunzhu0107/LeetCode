# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        # 2,4,16,37,9+49=58,25+64=89,64+81,145,1+16+25=42,16+4=20,4
        visited = set()
        while n not in visited:
            visited.add(n)
            total = 0
            while n > 0:
                n,digit = divmod(n,10)
                total += digit ** 2
            n = total
        return n == 1
            
        

class Solution:
    def getNext(self,n):
        happy_num = 0
        while n:
            happy_num += (n%10) ** 2
            n = n//10
        return happy_num
    
    def isHappy(self, n: int) -> bool:
        loop_check = set()
        
        while True:
            n = self.getNext(n)
            print(n)
            if n == 1:
                return True
            else:
                if n in loop_check:
                    return False
                else:
                    loop_check.add(n)