# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(r, prev):
            if r is None:
                return 0
            if r.val<prev:
                return good(r.left, prev)+good(r.right, prev)
            else:
                return 1 + good(r.left, r.val)+good(r.right, r.val)
            
        return good(root, root.val)
