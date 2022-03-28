# https://algo.monster/problems/lexicographically_smallest_string
def smallest_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    prev_c_ind = 0
    for i in range(1,len(s)):
        if s[i] < s[prev_c_ind]:
            return s[:prev_c_ind]+s[prev_c_ind+1:]
        prev_c_ind = i
    
    return s[:prev_c_ind]+s[prev_c_ind+1:]