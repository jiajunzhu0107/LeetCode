# https://leetcode.com/problems/reverse-linked-list/
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475919260&idx=1&sn=6538a2c8b9786f2c29236a1b001524c0&chksm=ff22e011c8556907e08fc50a4c242eb4754d5fdf0dc3a6ae837d3fd139872e6346c5fa9cad13&token=1029130343&lang=zh_CN#rd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or head.next == None:
            return head
        
        p = head
        q = None
        
        while p:
            temp = p.next
            p.next = q
            q = p
            p = temp
        
        return q