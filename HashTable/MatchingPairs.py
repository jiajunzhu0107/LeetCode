# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=559324704673058&c=370634718267911&ppid=454615229006519&practice_plan=0
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  curr_max = -2
  res = 0
  unmatched_s = {} #{b:{d}}
  unmatched_t = {}
  parsed_s = set()
  parsed_t = set()
  equal_pair_exist = False
  len_unmatched = 0 #1
  for i in range(len(s)):
    if s[i] == t[i]:
      res += 1
      if curr_max >= 2:
        continue
    else:
      if curr_max >= 2:
        continue
      if t[i] in unmatched_s: # 
        if s[i] in unmatched_s[t[i]]:
          curr_max = 2
          continue
        else:
          curr_max = 1
          if s[i] in unmatched_s:
            unmatched_s[s[i]].add(t[i])
          else:
            unmatched_s[s[i]] = {t[i]}
          if t[i] in unmatched_t:
            unmatched_t[t[i]].add(s[i])
          else:
            unmatched_t[t[i]].add(s[i])
          len_unmatched += 1
      else:
        if s[i] in unmatched_t:
          if t[i] in unmatched_t[s[i]]:
            curr_max = 2
            continue
          else:
            curr_max = 1
            if t[i] in unmatched_t:
              unmatched_t[t[i]].add(s[i])
            else:
              unmatched_t[t[i]] = {s[i]}
            if s[i] in unmatched_s:
              unmatched_s[s[i]].add(t[i])
            else:
              unmatched_s[s[i]].add(t[i])
            len_unmatched += 1
        else:
          unmatched_s[s[i]] = {t[i]}
          unmatched_t[t[i]] = {s[i]}
          len_unmatched += 1
          
    if not equal_pair_exist:
      if s[i] in parsed_s or t[i] in parsed_t:
        equal_pair_exist = True
      else:
        parsed_s.add(s[i])
        parsed_t.add(t[i])

			
  if curr_max > 0:
    return res + curr_max
  if equal_pair_exist:
    return res
  if len_unmatched == 1:
    return res - 1
  else:
    return res - 2

  
  











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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  