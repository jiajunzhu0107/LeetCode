#(), True
#(*), True
#(*)), True
#((*), True
# "", True
# *, True

#there're better ways
# check solution and discussion
class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        for char in s:
            
            if char in ('(', '*'):
                stack.append(char)
                # if char == '(':
                #     num_left += 1
                # else: #char == '*'
                #     num_star += 1
            else: # char == ')'
                matched = False
                num_star_popped = 0
                while stack:
                    item = stack.pop()
                    if item == '(':
                        stack += ['*'] * num_star_popped
                        matched = True
                        break
                    else:
                        num_star_popped += 1
                if not matched:
                    if num_star_popped > 0:
                        stack = ['*'] * (num_star_popped - 1)
                    else:
                        return False
        
        num_star_popped = 0
        while stack:
            item = stack.pop()
            if item == '*':
                num_star_popped += 1
            else:
                if num_star_popped > 0:
                    num_star_popped -= 1
                else:
                    return False
        return True