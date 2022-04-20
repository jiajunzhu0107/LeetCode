# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=840934449713537&c=370634718267911&ppid=454615229006519&practice_plan=1
def numberOfWays(arr, k):
  dic = {} #{1:{0},2:{1},3:{2}}
  res = 0
  for index, a in enumerate(arr):
    if k-a in dic:
      res += len(dic[k-a])
    if a not in dic:
      dic[a] = {index}
    else:
      dic[a].add(index)
  return res
