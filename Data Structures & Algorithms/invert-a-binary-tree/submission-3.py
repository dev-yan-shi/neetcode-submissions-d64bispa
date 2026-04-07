# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## BFS - queue approach
        if not root or (not root.left and not root.right):
            return root
        nodes = deque([root])
        while nodes:
            n = nodes.popleft()
            n.left, n.right = n.right, n.left
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)
        return root
        