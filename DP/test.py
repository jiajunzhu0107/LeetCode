from sortedcontainers import SortedList, SortedSet, SortedDict

a = SortedDict({5:1,2:2,3:3})
# if 1 not in a:
#     a[1] = [2]
print(a.peekitem(0))