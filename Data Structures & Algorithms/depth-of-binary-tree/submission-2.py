# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## BFS approach
        #[3] // [9,20] l=1 // [15, 7] l=2 // [] l=3
        level = 0
        nodes = deque()
        if not root:
            return 0
        nodes.append(root)
        while nodes:
            for i in range(len(nodes)):
                n = nodes.popleft()
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
            level+=1
        return level
        