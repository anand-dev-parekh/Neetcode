# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans

    def helper(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        l_height = self.helper(root.left)
        r_height = self.helper(root.right)

        if abs(l_height - r_height) > 1:
            self.ans = False
        
        return max(l_height, r_height) + 1