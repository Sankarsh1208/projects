# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            lrob, lskip = dfs(root.left)
            rrob, rskip = dfs(root.right)
            rob = root.val + lskip + rskip
            skip = (max(lrob, lskip) + max(rskip, rrob))
            return rob, skip
        return max(dfs(root))