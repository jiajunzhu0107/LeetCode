
a = [1,2]
b = []
# import copy
# c = copy.deepcopy(a)
c = a
b.append(c)
a.append(3)
print(b)

a = []
b = ''.join(a)
print(f'{b!r}')