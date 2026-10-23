#O(mn):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True
        
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and same(p.left, q.left) and same(p.right, q.right)
        if not root:
            return False
        return same(root, subRoot) or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

#O(m+n):
#converting the numbers into strings and comparing them with subRoot pointer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def stri(r):
            if not r:
                return ',#'
            return ','+str(r.val)+stri(r.left)+stri(r.right)
        return stri(subRoot) in stri(root)