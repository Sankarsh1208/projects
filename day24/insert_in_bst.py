# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, r: TreeNode | None, val: int) -> TreeNode | None:
        if not r:
            return TreeNode(val)
        if r.val>val:
            r.left = self.insertIntoBST(r.left, val)
        if r.val<val:
            r.right = self.insertIntoBST(r.right, val)
        return r
        
            