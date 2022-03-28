# https://algo.monster/problems/jump_game
# the test cases seems like incorrect
# the solution is reaching value == 0 instead of index == 0
def jump_game(arr: List[int], start: int) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    visited = [False] * len(arr)
    def dfs(i):
        #print(i)
        if (i < 0) or (i > (len(arr) -1)) or (visited[i]):
            return False
        elif i == 0:
            #print('True')
            return True
        else:
            visited[i] = True
            res = dfs(i-arr[i]) or dfs(i + arr[i])
            visited[i] = False
        return res
            
    return dfs(start)