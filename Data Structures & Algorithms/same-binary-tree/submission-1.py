# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        node_pairs = []
        if p.val != q.val:
            return False
        node_pairs.append((p.left,q.left))
        node_pairs.append((p.right, q.right))
        #print("current stack", node_pairs)
        while node_pairs:
            p,q = node_pairs.pop()
            if not p or not q:
                if not p and not q:
                    continue
                return False
            if p.val == q.val:
                node_pairs.append((p.left, q.left))
                node_pairs.append((p.right, q.right))
                #print("current stack", node_pairs)
            else:
                return False
            
        return True
            

        