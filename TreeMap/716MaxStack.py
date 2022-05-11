# https://leetcode.com/problems/max-stack/discuss/1552599/Python3-Doubly-linked-list-%2B-TreeMap-with-explaination

# check out above link for tree map solution
class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxHeap = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def peekMax(self) -> int:
        self.maxHeap = [(-1*val,idx) for idx,val in enumerate(self.stack)]
        heapify(self.maxHeap)
        return self.maxHeap[0][0] * -1

    def popMax(self) -> int:
        # print(self.stack)
        self.maxHeap = [(-1*val,-1*idx) for idx,val in enumerate(self.stack)]
        # print(self.stack)
        heapify(self.maxHeap)
        # print(self.stack)
        res,idx = heappop(self.maxHeap)
        self.stack.pop(-1*idx)
        # print(self.stack)
        # print(self.maxHeap)
        return -1*res
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()