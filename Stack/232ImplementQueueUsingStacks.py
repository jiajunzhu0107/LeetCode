# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.outStack:
            val = self.outStack.pop()
            return val
        else:
            while self.inStack:
                val = self.inStack.pop()
                self.outStack.append(val)
            return self.outStack.pop()
                
        

    def peek(self) -> int:
        val = self.pop()
        self.outStack.append(val)
        return val
        

    def empty(self) -> bool:
        if not (self.inStack or self.outStack):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()