# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dictionary = defaultdict(deque)
        curr_level = []

        
        stack = [[root, 0]]

        while stack:

            curr, level = stack.pop() 
            dictionary[level].appendleft(curr.val)
            
            
            if curr.left:
                stack.append([curr.left, level+1])
            if curr.right:
                stack.append([curr.right, level+1])
        
        res = []
        for key in dictionary:
            res.append(dictionary[key])

        return res





        