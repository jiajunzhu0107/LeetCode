# https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1#
# your task is to complete this function
# function should return false/0 if length is even
# else return true/1
def isLengthEvenOrOdd(head):
    # Code here
    # slow = head
    node = head
    l = 0
    while node:
        l += 1
        node = node.next

    if l % 2 == 0 :
        return 0
    else:
        return 1