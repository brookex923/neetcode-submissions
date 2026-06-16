# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        if not root:
            return True
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if node.left:
                    lefth = maxDepth(node.left)
                else:
                    lefth = 0
                if node.right:
                    righth = maxDepth(node.right)
                else:
                    righth = 0
                if abs(lefth - righth) > 1:
                    return False
        
                stack.append(node.left)
                stack.append(node.right) 
        
        return True