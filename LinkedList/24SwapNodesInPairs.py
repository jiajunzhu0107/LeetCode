
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475919380&idx=1&sn=f4564f6926b169e8f7820ade0d04af8f&chksm=ff22ef99c855668fe740cd03b4987eb0e11a33385e4813a03525a53712adcf51d121c7129235&token=1029130343&lang=zh_CN#rd
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(-1,head)
        pre = dummyHead
        p = head
        
        while p and p.next:
            q = p.next
            pre.next = q
            p.next = q.next
            q.next = p
            pre = p
            p = p.next
        return dummyHead.next