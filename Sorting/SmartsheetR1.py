#arr = [0,2,1,0,1,3]
#O(N*logn)
#O(N)


def mergeSort(arr): #[0,2]
  if len(arr) <= 1:
    return arr
  left = 0
  right = len(arr) - 1
  middle = (left + right) // 2
  #print(f'left:{arr[left:middle+1]}')
  #print(f'right:{arr[middle+1:len(arr)]}')
  left_part = mergeSort(arr[left:middle+1])
  right_part = mergeSort(arr[middle+1:len(arr)])
  #print(f'left_part:{left_part}')
  #print(f'right_part:{right_part}')
  return merge(left_part, right_part)
  
def merge(left_part, right_part):
  curr_left_ind = 0
  curr_right_ind = 0
  res = []
  while curr_left_ind < len(left_part) and curr_right_ind < len(right_part):
    if left_part[curr_left_ind] <= right_part[curr_right_ind]:
      res.append(left_part[curr_left_ind])
      curr_left_ind += 1
    else:
      res.append(right_part[curr_right_ind])
      curr_right_ind += 1
  if curr_left_ind < len(left_part):
    res += left_part[curr_left_ind:]
  if curr_right_ind < len(right_part):
    res += right_part[curr_right_ind:]
  return res  
arr = [0,2,1,0,1,3,-3]
#arr = [2,0]
arr = [3]
[0,1,2,3]

#max = 3
#min = 0
#[3,0,1,2]  #[3,0,1,3]
#[3,0,1,3]
#right = len(nums) - 1
#right - 1
#left = 0
#[1,0,3]
#right - 1
#left = 0
#[0,1]
#right - 1
#left = 0
#[0]
#n > n + 1
#n = len(nums) - 1
#3 n
#0 nums[0]
#left 
#right

def sortAlg2(arr):
  left_ind = 0
  right_ind = len(arr) - 1
  for i in range(left_ind, right_ind + 1):
    if i == 3:
      arr[i],arr[right_ind] = arr[right_ind], arr[i]
      right_ind -= 1
    elif i == 0:
      arr[i], arr[left_ind] = arr[left_ind], arr[i]
      left_ind += 1
    else:
      for:
        if arr[i] > arr[i+1]
    

res = mergeSort(arr)
print(res)
