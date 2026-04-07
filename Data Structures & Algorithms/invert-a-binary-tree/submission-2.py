# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## stack approach
        #[1,2,3,4,5,6.7]
        # [1] -> [2, 3] -> [2, 6, 7] -> [2, 6] -> [2] -> []
        # [1, 3, 2] -> [1,3,2,7,6] -> [4,5] ->
        if not root or (not root.left and not root.right):
            return root
        nodes = [root]
        while nodes:
            n = nodes.pop()
            if not n or (not n.left and not n.right):
                continue
            temp = n.left
            n.left = n.right
            n.right = temp
            nodes.append(n.right)
            nodes.append(n.left)
            
        return root
            
        