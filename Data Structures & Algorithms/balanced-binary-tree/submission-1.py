# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            if abs(self.getHeight(curr.left) - self.getHeight(curr.right)) > 1:
                return False
        
        return True
    

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        