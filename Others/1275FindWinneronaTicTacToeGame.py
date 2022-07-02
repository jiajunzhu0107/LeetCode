class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[''] * 3 for _ in range(3)]
        for index, [row, col] in enumerate(moves):
            if index % 2 == 0:
                current_marker = 'X'
            else:
                current_marker = 'O'
            
            grid[row][col] = current_marker
            # print(index, grid, row, col)
        for i in range(3):
            if grid[i] == ['X'] * 3:
                return "A"
            elif grid[i] == ['O'] * 3:
                return "B"
        
        for col in range(3):
            if grid[0][col] == "X" and grid[1][col] == "X" and grid[2][col] == "X":
                return "A"
            elif grid[0][col] == "O" and grid[1][col] == "O" and grid[2][col] == "O":
                return "B"
        
        if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
            return "A"
        if grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
            return "B"
        
        if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
            return "A"
        if grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
            return "B"
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"