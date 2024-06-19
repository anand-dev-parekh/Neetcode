
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        
        copy_head = cur_node = Node(0)
        node_map = {}

        while head:

            if head in node_map:
                new_node = node_map[head]
            else:
                new_node = Node(head.val)
            
            node_map[head] = new_node

            if head.random and head.random in node_map:
                new_node.random = node_map[head.random]
            elif head.random:
                new_node.random = Node(head.random.val)
                node_map[head.random] = new_node.random
                
            cur_node.next = new_node
            cur_node = new_node
            head = head.next
        
        return copy_head.next