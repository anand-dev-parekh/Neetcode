# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find midpoint of list
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 
        
        if fast.next:
            fast = fast.next
            slow = slow.next
        mid = slow


        # Reverse right side
        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node

            prev_node = slow
            slow = next_node

        # Two pointers: merge list
        while fast != mid:
            next_node = head.next
            head.next = fast
            head = next_node
            
            next_node = fast.next
            fast.next = head
            fast = next_node

        return