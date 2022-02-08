#https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #hash table
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_b = set()
        
        while headB is not None:
            nodes_in_b.add(headB)
            headB = headB.next
        
        while headA is not None:
            if headA in nodes_in_b:
                return headA
            headA = headA.next
        return None

    #two pointers
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        
        while pa != pb:
            if pa is None:
                pa = headB
            else:
                pa = pa.next
                
            if pb is None:
                pb = headA
            else:
                pb = pb.next
        return pa