# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class MyLinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        if index <0 or index >= self.length:
            return -1
        p = self.head
        for _ in range(index+1):
            p = p.next
        return p.val
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
    
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.length:
            return
        p = self.head
        addNode = Node(val)
        for _ in range(index):
            p = p.next
        addNode.next = p.next
        p.next = addNode
        
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index <0 or index >= self.length:
            return
        p = self.head
        for _ in range(index+1):
            pre = p
            p = p.next
        pre.next = p.next
        p = None
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)