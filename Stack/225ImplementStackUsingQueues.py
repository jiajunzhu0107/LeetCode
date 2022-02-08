# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.main_queue = []
        self.help_queue = []

    def push(self, x: int) -> None:
        self.help_queue.append(x)
        while self.main_queue:
            val = self.main_queue.pop(0)
            self.help_queue.append(val)
        self.main_queue = self.help_queue
        self.help_queue = []
                 
    def pop(self) -> int:
        return self.main_queue.pop(0)

    def top(self) -> int:
        return self.main_queue[0]

    def empty(self) -> bool:
        if not self.main_queue:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()