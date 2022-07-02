# Question 1: Check valid parentheses

# Examples:
# Input: s = "()"
# Output: true
# 
# Input: s = "()[]{}"
# Output: true

# invalid input "(abc)"
# invalid set of parentheses (valid input): "((]())["

# [()][] true

# "" true
# "[" False
# "]" False
# "()" true
# "{[()]}" true
# "()[]{}" true
# "()["

def isValid(s):
    stack = []
    for c in s:
        if c in ("(", "[", "{"):
            stack.append(c)
        else: # right parentheses
            if not stack:
                return False
            left = stack.pop()
            if c == ")":
                if left != "(":
                    return False
            elif c == "]":
                if left != "[":
                    return False
            else: # c == "}"
                if left != "{":
                    return False
    if len(stack) > 0:
        return False
    return True


# You are standing on the top left corner of an m x n grid (i.e., grid[0][0]). You want to move to the bottom right corner (i.e., grid[m - 1][n - 1]). You can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that you can take to reach the bottom-right corner.
# m, n >= 2

# |-----|-----|-----|-----|-----|-----|-----|
# |  X  |     |     |     |     |     |     |
# |-----|-----|-----|-----|-----|-----|-----|
# |     |Goal2|     |     |     |     |     |
# |-----|-----|-----|-----|-----|-----|-----|
# |     |Goal3|Goal4|     |     |     |Goal |
# |-----|-----|-----|-----|-----|-----|-----|


# |-----|-----|-----|-----|-----|-----|-----|
# |  1  |  1   |  1   |     |     |     |     |
# |-----|-----|-----|-----|-----|-----|-----|
# |  1   | 2  |  3  |     |     |     |     |
# |-----|-----|-----|-----|-----|-----|-----|
# |  1   | 3  |   6|     |     |     |Goal |
# |-----|-----|-----|-----|-----|-----|-----|

# Examples: 
# Input: m = 3, n = 7
# Output: 28

# 2 ^ (m * n)

# (3 - 1 ) * (7 - 1) * 2 = 24
# 24 + 2 + 6 = 32

# 3 * 3
# 6

# 2 * 2
# 2

# 2 * 3 = (2*2) + (1*3) = 2 + 1
# 3 * 3 = (2*3)3 + (3*2)3 = 6

# 1 * 1 = 1
# 1 * 2 = (1*1) + (0*2)/0 = 1
# 2 * 2

# m * n

# 2 * 3
def numPath(m, n):
    dp = [[0] * n] * m
    for i in range(n):
        dp[0][i] = 1
    for i in range(m):
        dp[i][0] = 1
    
    for row in range(1,m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    
    return dp[m-1][n-1]




# every path involves (m-1) + (n-1) steps
# for m = 7, n = 3, steps = 8
# in every path, m-1 steps will be going down, and n-1 will be going right
# _ , _ , _ , _ , _ , _ , _ , _ - you have to choose 2 blanks for going down (or you can choose 6 blanks for going right)
# (m+n-2)C(m-1) = (m+n-2)C(n-1)