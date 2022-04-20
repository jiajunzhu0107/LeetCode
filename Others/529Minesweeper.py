# https://leetcode.com/problems/minesweeper/
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        revealed = set()
        def reveal(row, col):
            if (row,col) in revealed:
                return
            revealed.add((row,col))
            count = 0
            
            for row_delta in range(max(0,row-1),min(len(board),row+2)):
                for col_delta in range(max(0,col-1),min(len(board[0]),col+2)):
                    if board[row_delta][col_delta] == 'M':
                        count += 1
            if count > 0:
                board[row][col] = str(count)
                return
            else:
                board[row][col] = 'B'
                for row_delta in range(max(0,row-1),min(len(board),row+2)):
                    for col_delta in range(max(0,col-1),min(len(board[0]),col+2)):
                        reveal(row_delta, col_delta)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'

        else:
            reveal(click[0], click[1])
        return board  

#https://techdevguide.withgoogle.com/resources/former-interview-question-minesweeper/#!
import random
class Matrix:
	def __init__(self, rows, cols, cellType):
		self._cellType = cellType
		self.resize(rows, cols)
	
	def resize(self, rows, cols):
		self._rows = rows
		self._cols = cols
		self._data = [self._cellType for i in range(self._rows * self._cols)]	
	def rows(self):
		return self._rows
	def cols(self):
		return self._cols
	def at(self, row, col):
		return self._data[self._cols * row + col]


class Minesweeper:
	class Cell:
		def __init__(self):
			self.value = 0
			self.visible = False
	def __init__(self, rows, cols, num_mines):
		self._matrix = Matrix(rows, cols, self.Cell())
		self.rows = rows
		self.cols = cols
		mine_list = [9]*num_mines + [0]*(rows * cols - num_mines)
		random.shuffle(mine_list)
		for index, v in enumerate(mine_list):
			if v == 9:
				row = index//cols
				col = index % cols
				self._matrix.at(row,col).value = 9
				for r in range(max(0,row-1),min(rows,row+2)):
					for c in range(max(0,col-1),min(cols,col+2)):
						if r == 0 and c == 0:
							continue
						if self._matrix.at(r,c).value != 9:
							self._matrix.at(r,c).value += 1
	
	def click(self, row, col):
		if row > self.rows or row < 0 or col > self.cols or col < 0:
			return False
		cell = self._matrix.at(row,col)
		if cell.visible:
			return False
		cell.visible = True
		if cell.value == 9:
			print('BOOM!')
			return True
		elif cell.value != 0:
			return False
		else:
				self.click(row+1,col)
				self.click(row-1,col)
				self.click(row,col-1)
				self.click(row,col+1)
			
		return False
	def print(self):
		for r in self.rows:
			for c in self.cols:
				if self._matrix.at(r,c).visible:
					print(self._matrix.at(r,c).value, end=' ')
				else:
					print('-', end = ' ')
			print()
		print()