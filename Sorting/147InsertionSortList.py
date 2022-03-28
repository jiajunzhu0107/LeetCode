# https://leetcode.com/problems/insertion-sort-list/
# Definition for singly-linked list.
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head_temp = ListNode()
        current_sorted_node = sorted_head_temp
        # unsorted_head_temp = ListNode(0,head)
        current_unsorted_node = head
        while current_unsorted_node is not None:
            if current_sorted_node.next is None:
                current_sorted_node.next = ListNode(current_unsorted_node.val)
            else:
                while(current_sorted_node.next is not None):
                    if current_unsorted_node.val < current_sorted_node.next.val: #stable sort 
                        break
                    else:
                        current_sorted_node = current_sorted_node.next
                temp = current_sorted_node.next
                current_sorted_node.next = ListNode(current_unsorted_node.val)
                current_sorted_node.next.next = temp
            current_unsorted_node = current_unsorted_node.next
            current_sorted_node = sorted_head_temp
        
        return sorted_head_temp.next