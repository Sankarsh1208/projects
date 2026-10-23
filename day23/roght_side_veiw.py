# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        res = []
        def side(r, depth):
            if not r:
                return
            if len(res) == depth:
                res.append(r.val)
            side(r.right, depth+1)
            side(r.left, depth+1)
        side(root, 0)
        return res