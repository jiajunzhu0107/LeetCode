# https://algo.monster/problems/day_of_week
def day_of_week(day: str, k: int) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    mapping = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    ind = -1
    for i in range(len(mapping)):
        if mapping[i] == day:
            ind = i
            break
    return mapping[(ind + 1 + k) % 7 - 1]
a = [0]
cnt = 0
for i in range(1,5):
    for j in a:
        a.append(i)
        print(j)
        print(a)
        cnt += 1
        if cnt == 3:
            break
    break