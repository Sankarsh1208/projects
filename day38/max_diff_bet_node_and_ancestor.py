# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        def dfs(root, minv, maxv):
            if not root:
                return 0
            minv = min(root.val, minv)
            maxv = max(root.val, maxv)
            if not root.left and not root.right:
                return maxv-minv
            return max(dfs(root.left, minv, maxv), dfs(root.right, minv, maxv))
        return dfs(root, root.val, root.val)
        