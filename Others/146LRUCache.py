# https://leetcode.com/problems/lru-cache/

from collections import deque

class LRUCache:
    
    class DLL:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.DLL(0,0)
        self.tail = self.DLL(0,0)
        print(self.head)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.data:
            print(self.data[key])
            
            self.data[key].next.prev = self.data[key].prev
            self.data[key].prev.next = self.data[key].next
            
            self.data[key].next = self.head.next
            self.data[key].prev = self.head
            
            self.head.next.prev = self.data[key]
            self.head.next = self.data[key]
            return self.data[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            val = self.get(key)
            self.data[key].val = value
        else:
            new_head = self.DLL(key,value)
            self.size += 1
            if self.size > self.capacity:
                # print(self.tail.prev.val)
                # print(self.data)
                self.data.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                self.size -= 1
            new_head.next = self.head.next
            new_head.prev = self.head
            self.head.next.prev = new_head
            self.head.next = new_head
            self.data[key] = new_head
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)