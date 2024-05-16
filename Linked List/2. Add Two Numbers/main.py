# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_val, l2_val = 0, 0

        digit_pos = 1
        while l1 and l2:
            l1_val += digit_pos * l1.val
            l2_val += digit_pos * l2.val

            l1 = l1.next
            l2 = l2.next
            digit_pos *= 10
        
        if l1:
            l1_val += self.finishAdd(l1, digit_pos)
        elif l2:
            l2_val += self.finishAdd(l2, digit_pos)
        
        val = (l1_val + l2_val) // 10
        head_node = ListNode((l1_val + l2_val) % 10)
        cur_node = head_node
        while val > 0:
            node_val = val % 10
            val = val // 10
            cur_node.next = ListNode(node_val)
            cur_node = cur_node.next
        
        return head_node
    
    def finishAdd(self, li: ListNode, digit_pos: int) -> int:
        res = 0
        while li:
            res += digit_pos * li.val
            li = li.next
            digit_pos *= 10
        return res


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0

        ans = cur_node = ListNode()
        while l1 and l2:
            val = l1.val + l2.val + carry

            node_val = val % 10
            carry = (val - node_val) // 10

            l1 = l1.next
            l2 = l2.next

            cur_node.next = ListNode(node_val)
            cur_node = cur_node.next

        if l1:
            carry, cur_node = self.finishAdd(l1, carry, cur_node)
        elif l2:
            carry, cur_node = self.finishAdd(l2, carry, cur_node)
        
        if carry != 0:
            cur_node.next = ListNode(carry)


        return ans.next
    
    def finishAdd(self, li: ListNode, carry: int, cur_node: ListNode) -> tuple:
        while li:
            val = li.val + carry

            node_val = val % 10
            carry = (val - node_val) // 10

            li = li.next
            cur_node.next = ListNode(node_val)
            cur_node = cur_node.next

        return carry, cur_node
