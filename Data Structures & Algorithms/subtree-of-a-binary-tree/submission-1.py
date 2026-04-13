# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, root1: Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        # if not root1 and not root2:
        #     return True
        # if not root1 or not root2 or root1.val != root2.val:
        #     return False
        stack = [(root1, root2)]
        while stack:
            p,q = stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val!=q.val:
                return False
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True
              
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        stack = [root]
        while stack:
            n = stack.pop()
            if self.isSameTree(n, subRoot):
                return True
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        
        return False

            


        