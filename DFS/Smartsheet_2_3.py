#Coding Question:
#Given a Grid, find maximum number of connected colors


#Char [][] grid = {
#{'r', 'g', 'r'},
#{'r', 'g', 'r'},
#{'r', 'g', 'r'}
#};
# any chars, len(c) == 1
# return 3

#{'r':{(xi, yi),(),()},'b':}

*/

def childrenOfNode(r, c):
  for r,c in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
    yield r,c
    
def isValidChild(parsed, r, c):
  

def maxConnectedColors(grid):
  max_res = 0
  res = 0
  if len(grid) < 0:
    return res
  parsed = set()
  #o(N*M)
  
  def dfs(node_r, node_c, parsed):
    current_color = grid[node_r][node_c]
    if not isValidChild(parsed, r, c): # color match, within boundary, not parsed
      return 
    parsed.add((node_r, node_c))
    res += 1
    for r, c in childrenOfNode(node_r, node_c): #four children
      if grid[r][c] == node:
        dfs(r,c)
    return
        
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if (i,j) not in parsed:
        dfs(i,j)
        max_res = max(max_res, res)
        res = 0
  return max_res
  