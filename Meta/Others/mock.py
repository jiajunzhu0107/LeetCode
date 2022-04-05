# indexOfAnagram("facebook", "book") == 4
#                 01234
# indexOfAnagram("facebook", "boko") == 4
# indexOfAnagram("facebook", "bokx") == -1

# indexOfAnagram("facebookbook", "book") == 4

# indexOfAnagram("faceabcooookabc", "ookabc") == 4

""


from collections import deque, Counter

def indexOfAnagram(str1, str2):
    # index_of_first = {
    #     c:-1 for c in str2
    # }
    remained = Counter(str2)
    print(remained)
    queue = deque([])
    # res = -1

    for index, c in enumerate(str1):
        # print(queue)
        if c not in remained:
            continue
        else:   
            if remained[c] <= 0:
                while len(queue) > 0:
                    pop_char,ind = queue.popleft()
                    remained[pop_char] += 1
                    if pop_char == c:
                        break
            remained[c] -= 1
            queue.append((c, index))
        print(queue)
        if len(queue) == len(str2):
            _,res = queue.popleft()
            return res
    return -1

res = indexOfAnagram('faceboooookboob','okbo')
                    #   0123456789
print(res)
    



