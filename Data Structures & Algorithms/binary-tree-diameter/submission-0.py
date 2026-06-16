# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        diameter = leftHeight + rightHeight 
        children = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, children)


    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


        
        
        