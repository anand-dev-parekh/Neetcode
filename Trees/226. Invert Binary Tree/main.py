# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        
        right_tree = self.invertTree(root.right)
        left_tree = self.invertTree(root.left)

        root.left = right_tree
        root.right = left_tree
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
