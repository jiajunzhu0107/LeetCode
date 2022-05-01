import copy


class foo:
    def __init__(self) -> None:
        self.val = 0

a = foo()
a.val = 1
print(a.val)
b = copy.deepcopy(a)
print(b.val)
b.val = 2
print(b.val)
print(a.val)


print('*****')
a = [1]
b = a
a.append(2)
print(b)