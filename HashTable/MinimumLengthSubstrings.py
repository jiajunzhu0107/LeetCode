
# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2237975393164055&c=370634718267911&ppid=454615229006519&practice_plan=0
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

#t = fad
#s = dbbabbbfdad
from collections import Counter
from math import inf
#s = "ddcbdfebebce"
#t = "fd"
def min_length_substring(s, t):
  # Write your code here
  left = 0
  right = 0
  cnt_dic = Counter(t)
  missings = len(t)
  isExpanding = True
  res = inf
  while right < len(s): #double check
    if isExpanding:
       if s[right] not in cnt_dic:
          right += 1
          continue
       else:
          cnt_dic[s[right]] -= 1
          missings -= 1 if cnt_dic[s[right]] >= 0 else 0
          if missings <= 0:
            isExpanding = False
            res = min(res,right-left+1)
          else:
            right += 1
    else:
        if s[left] not in cnt_dic:
          left += 1
          if right - left + 1 < len(t):
            isExpanding = True
            right += 1
        else:
          cnt_dic[s[left]] += 1
          missings += 1 if cnt_dic[s[left]] > 0 else 0
          if missings > 0:
            isExpanding = True
            right += 1
          else:
            res = min(res,right-left+1)
            left += 1
            if right - left + 1 < len(t):
              isExpanding = True
              right += 1
            
          

  return res if res != inf else -1









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  