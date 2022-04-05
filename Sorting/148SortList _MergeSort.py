# https://algo.monster/problems/sorting_intro
# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #merge sort
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        right = self.sortList(mid.next) 
        # if mid.next is None, then only one node, then head == mid, then head.next is None, returned already
        mid.next = None
        left = self.sortList(head)
        
        
        tail = ListNode()
        temp_head = tail
        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left is not None:
            tail.next = left
        else:
            tail.next = right
        
        return temp_head.next
    
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow