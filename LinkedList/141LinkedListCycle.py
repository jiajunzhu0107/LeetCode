# https://leetcode.com/problems/linked-list-cycle/
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475919540&idx=1&sn=12f2bdd8f46f3c019301a402f02832bb&chksm=ff22ef39c855662fd64370a619e8d1164343e1f36c053593f67abef9ef333bb68007f787238f&token=1029130343&lang=zh_CN#rd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False