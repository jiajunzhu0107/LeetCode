# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
# 2018. Check if Word Can Be Placed In Crossword

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # by row
        
        length_word = len(word)
        for row in board:
            current_length = 0
            positive_direction = True
            reverse_direction = True
            for cell in row:
                if cell == '#':
                    if current_length == length_word and (positive_direction or reverse_direction):
                        return True
                    current_length = 0
                    positive_direction = True
                    reverse_direction = True
                elif cell == ' ':
                    current_length += 1
                else: # cell is a letter
                    index = current_length
                    current_length += 1
                    if current_length <= length_word:
                        if word[index] != cell:
                            positive_direction = False
                        if word[-index-1] != cell:
                            reverse_direction = False
            if current_length == length_word and (positive_direction or reverse_direction):
                return True
        
        # by col       
        for col in range(len(board[0])):
            current_length = 0 
            positive_direction = True
            reverse_direction = True
            for i in range(len(board)):
                cell = board[i][col]
                if cell == '#':
                    if current_length == length_word and (positive_direction or reverse_direction):
                        return True
                    current_length = 0
                    positive_direction = True
                    reverse_direction = True
                elif cell == ' ':
                    current_length += 1
                else: # cell is a letter
                    index = current_length
                    current_length += 1
                    # print(index)
                    if current_length <= length_word:
                        if word[index] != cell:
                            positive_direction = False
                        if word[-index-1] != cell:
                            reverse_direction = False
            if current_length == length_word and (positive_direction or reverse_direction):
                return True
        return False
                

                        