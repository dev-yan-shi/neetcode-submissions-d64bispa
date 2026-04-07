# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # [(1,1)], [(2,2), (3,2)] // [(2,2) (4,3)] // []
        if not root:
            return 0
        res = 1
        stack = [(root, 1)]
        while stack:
            (n, depth) = stack.pop()
            res = max(res, depth)
            if not n.left and not n.right:
                continue
            if n.left:
                stack.append((n.left, depth+1))
            if n.right:
                stack.append((n.right, depth + 1))
        return res
              
            
        