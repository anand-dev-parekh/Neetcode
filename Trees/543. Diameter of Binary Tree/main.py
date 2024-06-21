# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root)[1]
        
    def helper(self, root):
        if root == None:
            return 0, 0

        l_edge_max, l_dis_max = self.helper(root.left)
        r_edge_max, r_dis_max = self.helper(root.right)

        return 1 + max(l_edge_max, r_edge_max), max(l_dis_max, r_dis_max, l_edge_max + r_edge_max)