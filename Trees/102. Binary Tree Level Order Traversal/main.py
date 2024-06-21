from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        ans = []
        queue = deque([(root, 0)])

        while queue:
            node, i = queue.popleft()

            if i >= len(ans):
                ans.append([node.val])
            else:
                ans[i].append(node.val)

            if node.left: queue.append((node.left, i+1)) 
            if node.right: queue.append((node.right, i+1)) 
        
        return ans

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:

            l = len(queue)
            level = []
            for _ in range(l):

                node = queue.popleft()
                level.append(node.val)


                if node.left: queue.append(node.left) 
                if node.right: queue.append(node.right) 

            ans.append(level) 

        return ans