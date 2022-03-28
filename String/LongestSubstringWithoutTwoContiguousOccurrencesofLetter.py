# https://algo.monster/problems/longest_substring_without_3_contiguous_occurrences_letter
def longestValidString(str) -> str:
      # WRITE YOUR BRILLIANT CODE HERE
    prev_c = ''
    cnt = 0
    left = 0
    right = 0
    max_length = 0
    current_length = 0
    res = ''
    while right < len(str):
        if str[right] == prev_c:
            cnt += 1
            if cnt > 2:
                left = right - 1
        else:
            cnt = 1    
        current_length = right - left + 1
        if current_length > max_length:
            res = str[left:right+1]
        max_length = max(max_length, current_length)
        prev_c = str[right]
        right += 1
        
    return res