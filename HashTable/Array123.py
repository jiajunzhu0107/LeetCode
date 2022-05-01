# https://codingbat.com/prob/p193604
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
def array123(nums):
  remain = {1,2,3}
  for n in nums:
    if n in remain:
      remain.remove(n)
      if len(remain) <= 0:
        return True
  return False
