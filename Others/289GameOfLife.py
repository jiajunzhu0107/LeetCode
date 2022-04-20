import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_board = copy.deepcopy(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if temp_board[r][c] == 1:
                    cnt = 0
                    for r_d in range(-1,2):
                        for c_d in range(-1,2):
                            if r + r_d < 0 or r + r_d >= len(board) or c+c_d < 0 or c+c_d >= len(board[0]) or (r_d == 0 and c_d == 0):
                                continue
                            if temp_board[r+r_d][c+c_d] == 1:
                                cnt += 1
                    if cnt < 2 or cnt > 3:
                        # print('die')
                        board[r][c] = 0
                        # print(r, c)
                        # print(temp_board)
                else:
                    cnt = 0
                    for r_d in range(-1,2):
                        for c_d in range(-1,2):
                            if r + r_d < 0 or r + r_d >= len(board) or c+c_d < 0 or c+c_d >= len(board[0]) or (r_d == 0 and c_d == 0):
                                continue
                            if temp_board[r+r_d][c+c_d] == 1:
                                cnt += 1
                    if cnt == 3:
                        # print('revive')
                        board[r][c] = 1
        board = temp_board
        # print(temp_board)
        # print(board)
        