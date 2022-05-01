# https://www.coderbyte.com/editor/First%20Factorial:Python3
# First Factorial
# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
# Examples
# Input: 4
# Output: 24
# Input: 8
# Output: 40320
def FirstFactorial(num):
  res = 1
  for n in range(num,0,-1):
    res *= n

  # code goes here
  return res

# keep this function call here 
print(FirstFactorial(input()))