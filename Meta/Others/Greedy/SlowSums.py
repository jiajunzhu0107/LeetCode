# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=836241573518034&c=370634718267911&ppid=454615229006519&practice_plan=0
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
from heapq import heapify, heappush, heappop

def getTotalTime(arr):
  # Write your code here
  #max heap
  heap = [-1 * a for a in arr]
  heapify(heap)
  res = 0
  while len(heap) > 1:
    max_1 = heappop(heap) * -1
    max_2 = heappop(heap) * -1
    penalty = max_1 + max_2
    res += penalty
    heappush(heap, penalty * -1)
  return res
  









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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  