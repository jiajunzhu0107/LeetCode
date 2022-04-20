# https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!

def findLongestWord(s, d): # s: abppplee, d:{"able", "ale", "apple", "bale", "kangaroo"}
	s_dic = {} # {a:[0], b:[2], p:[2,3,4], l:[5], e:[6,7]}
	for i in range(s):
		if s[i] not in s_dic:
			s_dic[s[i]] = [i]
		else:
			s_dic[s[i]].append(i)
	sort_lst = sorted([(-len(w), w) for w in d])
	for _,word in sort_lst:
		res = isSubsequence(word, s_dic)
		if res:
			return word
	return None

def isSubsequence(word, s_dic):
	curr_ind = -1
	for c in word:
		if c in s_dic:
			index = findMinIndexLargerThanTarget(s_dic[c], curr_ind)
			if index is None:
				return False
			else:
				curr_ind = index
		else:
			return False
	return True

def findMinIndexLargerThanTarget(list_index, target):
	left = 0
	right = len(list_index) - 1
	res = None
	while left <= right:
		mid = (left + right) // 2
		if list_index[mid] > target:
			res = list_index[mid] #potential res
			right = mid - 1
		else:
			left = mid + 1
	return res

res = findLongestWord(s, d)
