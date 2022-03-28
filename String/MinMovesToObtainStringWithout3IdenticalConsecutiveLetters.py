# https://algo.monster/problems/min_moves_no_three_consecutive_chars
def min_moves(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    cnt = 0
    res = 0
    prev_c = ''
    for i,c in enumerate(s):
        if c == prev_c:
            cnt += 1
            if cnt == 3:
                if i == len(s) - 1:
                    return res + 1
                if s[i+1] != c:
                    #filp previous char
                    cnt = 1
                    res += 1
                else:
                    #flip current char
                    prev_c = '' #we know that after flipped, the next one will be different , so doesn't matter
                    cnt = 1
                    res += 1
        else:
            cnt = 1      
            prev_c = c
        
    return res