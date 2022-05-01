# https://leetcode.com/problems/design-bitset/

class Bitset:

    def __init__(self, size: int):
        self.data = 0 #integer in python could have infinite number of bits, only neccessary spaces will be allocated
        self.size = size
	
        

    def fix(self, idx: int) -> None:
        if idx < self.size:
            self.data |= 1 << (self.size - idx - 1) 
        # print('fix: ', bin(self.data))

    def unfix(self, idx: int) -> None:
        if (idx < self.size) and (self.data & 1 << (self.size - idx - 1) ):
            # print(idx)
            # print(bin(self.data))
            # print(bin(~(1 << idx)))
            self.data ^= 1 << (self.size - idx - 1) 
            # print('unfix: ',bin(self.data))

    def flip(self) -> None:
        self.data ^= (1<<self.size) - 1
        # print('flip: ',bin(self.data))

    def all(self) -> bool:
        return self.data == int('1'*self.size, 2)

    def one(self) -> bool:
        return self.data != 0

    def count(self) -> int:
        return self.data.bit_count()
        

    def toString(self) -> str:
        b = bin(self.data)[2:]
        return '0' * (self.size - len(b)) + b
