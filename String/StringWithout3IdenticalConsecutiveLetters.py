# https://algo.monster/problems/string_without_3_identical_consecutive_letters
def filter_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    prev_c = ''
    cnt = 0
    res = []
    for i in range(len(s)):
        if s[i] == prev_c:
            cnt += 1
            if cnt == 3:
                cnt -= 1
                continue
        else:
            prev_c = s[i]
            cnt = 1
        res.append(s[i])

                
    return ''.join(res)
a = [3,2,1]
for i in a[:-1]:
    print(i)