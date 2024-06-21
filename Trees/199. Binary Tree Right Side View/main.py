from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:

            l = len(queue)
            ans.append(101)
            for _ in range(l):
                node = queue.popleft()

                ans[-1] = node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        return ans