# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_val, q_val = p.val, q.val

        while root:

            if root.val > p_val and root.val > q_val:
                root = root.left 
            elif root.val < p_val and root.val < q_val:
                root = root.right
            else:
                return root

        return None