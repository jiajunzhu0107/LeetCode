from collections import deque

a = deque([])
a.appendleft(8)
a.appendleft(2)
b = [1,3]
print(b+a)