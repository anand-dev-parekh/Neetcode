# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.findPath(root)

        return self.ans
    
    def findPath(self, root):
        if root == None:
            return 0

        l_path = self.findPath(root.left)
        r_path = self.findPath(root.right)

        max_path = max(l_path, r_path, 0) + root.val
        self.ans = max(max_path, self.ans, l_path + r_path + root.val)

        return max_path