from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node:
                output += str(node.val) + "d"
            else:
                output += "nd"
                continue

            queue.append(node.left)
            queue.append(node.right)

        return output
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        trees = data.split("d")
        trees = [x for x in trees if x != ""]

        if trees[0] == "n":
            return None

        node_beg = TreeNode(int(trees[0]))
        queue = deque([node_beg])
        i = 0
        while queue:
            node = queue.popleft()

            if node == None:
                continue

            i += 1
            l_tree_val = trees[i]
            if l_tree_val == "n" :
                node.left = None
            else:
                node.left = TreeNode(int(l_tree_val))
            queue.append(node.left)

            i += 1
            r_tree_val = trees[i]
            if r_tree_val == "n":
                node.right = None
            else:
                node.right = TreeNode(int(r_tree_val))
            queue.append(node.right)
        
        return node_beg



        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))