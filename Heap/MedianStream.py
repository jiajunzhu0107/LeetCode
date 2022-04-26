# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=547645422524434&c=370634718267911&ppid=454615229006519&practice_plan=0

import math

from heapq import heappush, heappop
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMedian(arr): #[1, 2], [5, 15, 1, 3]
	left = [] # max heap [-3, -1
	right = [] # min heap [5, 15
	res = [] #[5, 10, 5, 4]
	for a in arr:
		if len(left) > len(right):
			if a >= -1 * left[0]:
				heappush(right, a)
			else:
				heappush(right, -1 * heappop(left))
				heappush(left, -a)
		else: # len(left) can't < len(right)
			if len(right) <= 0 or a <= right[0]:
				heappush(left, -a)
			else:
				heappush(left, -1 * heappop(right))
				heappush(right, a)
		if len(left) > len(right):
			mid = -1 * left[0]
		else: # len(left) can't < len(right)
			mid = (-1 * left[0] + right[0]) // 2
		res.append(mid)
	return res

			

  
  
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  