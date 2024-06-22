from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, root, minVal, maxVal):
        if root == None:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False
        
        return self.isValid(root.left, minVal, root.val) and self.isValid(root.right, root.val, maxVal)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        stack = deque()
        prev_val = float('-inf')


        while root != None or len(stack) >= 1:
            while root != None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= prev_val:
                return False
            
            prev_val = root.val
            root = root.right

        return True