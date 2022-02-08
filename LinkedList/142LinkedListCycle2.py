# https://leetcode.com/problems/linked-list-cycle-ii/
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475919611&idx=1&sn=cebf6321b9d87cd7b2eb94e7c1bc8bb2&chksm=ff22ef76c8556660b42516720fbb7a5c946d419eddf88056bd77f6036d7f191c63fec6a683e1&token=1029130343&lang=zh_CN#rd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag1 = head
                flag2 = fast
                
                while flag1 != flag2:
                    flag1 = flag1.next
                    flag2 = flag2.next
                return flag1
        return None