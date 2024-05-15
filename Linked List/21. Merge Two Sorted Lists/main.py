# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ans = ListNode()

        cur_node = ans
        while list1 and list2:
            if list1.val < list2.val:
                min_node = list1
                list1 = list1.next
            else:
                min_node = list2
                list2 = list2.next

            cur_node.next = min_node
            cur_node = min_node

        if list1 or list2:
            cur_node.next = list1 if list1 else list2
            
        return ans.next

            


        