# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = slow = head 
        for _ in range(n):
            fast = fast.next 

        prev = slow
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next

        if prev == slow:
            return head.next

        prev.next = slow.next

        return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = head 
        slow = start = ListNode(next=head)

        for _ in range(n):
            fast = fast.next 

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return start.next