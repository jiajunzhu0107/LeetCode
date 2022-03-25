# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(res, path):
            if len(path) == len(digits):
                if len(path) > 0:
                    res.append(''.join(path))
                return
            current_num = digits[len(path)]
            for c in mapping[current_num]:
                path.append(c)
                backtrack(res, path)
                path.pop()
                
        res = []
        path = []
        backtrack(res, path)
        return res
                