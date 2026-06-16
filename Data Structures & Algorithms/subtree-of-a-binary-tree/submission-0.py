# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursively traverse through and see if it matches 
        if not root and not subRoot:
            return True
        
        stack = [root]

        while stack:
            curr = stack.pop()
            if self.isEqual(curr, subRoot):
                return True

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return False
            




    def isEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isEqual(root.left, subRoot.left) and self.isEqual(root.right, subRoot.right)
        else:
            return False
        