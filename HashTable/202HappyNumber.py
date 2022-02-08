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