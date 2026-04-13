# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        main_stack = [root]
        while main_stack:
            r = main_stack.pop()
            subStack = [(r, subRoot)]
            flag = True
            while subStack:
                p,q = subStack.pop()
                if not p and not q:
                    continue
                if not p or not q or p.val!=q.val:
                    flag = False
                    break

                subStack.append((p.left, q.left))
                subStack.append((p.right, q.right))

            if flag:
                return True
            if r.left:
                main_stack.append(r.left)
            if r.right:
                main_stack.append(r.right)
        return False
            
                    
            
                