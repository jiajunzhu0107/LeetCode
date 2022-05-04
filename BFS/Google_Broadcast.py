"""
"Chaining Broadcast Signals"

Let's define a kind of message called "Broadcast & Shut Down." When a router receives this message, it broadcasts the same message to all other routers within its wireless range (10 feet). 
Then, that router shuts down, and can no longer send or receive messages.

Given a list of router coordinates, tell me whether Router J can send this signal to Router K.
"""
[[x1,y1],[x2,y2],...,[xj,yj],...,[xk,yk],...,]


#O(N**2) -- time
#O(N) -- space
from collections import deque
def Broadcast(routers,start,end): [[0,0],[10,0],[5,0],[100,0], [20,0]], j = 0, k = 4
  queue = deque([start]) #[2,4]
  visited = {start} # {0,1,2,4}
  while queue:
    node_idx = queue.popleft() #1
    if node_idx == end:
      return True
    x_node, y_node = routers[node_idx] #0,0
    for i in range(routers): # optimize?
      xr, yr = routers[i]
      if i not in visited:
        if sqrt((y_node - yr)**2 + (x_node - xr)**2) <= 10:
          queue.append(i)
          visited.add(node_idx)
  return False
