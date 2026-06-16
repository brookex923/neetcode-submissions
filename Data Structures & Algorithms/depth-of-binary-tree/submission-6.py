# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #iterative dfs
        stack = []
        if root:
            stack.append([root, 1])
        res = 0
        while stack:
            popped, depth = stack.pop()
            if popped:
                res = max(res, depth)
            if popped.right:
                stack.append([popped.right, depth+1])
            if popped.left:
                stack.append([popped.left, depth+1])
        
        return res
