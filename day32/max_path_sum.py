# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxn = float('-inf')
        def dfs(root):
            nonlocal maxn
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            maxn = max(maxn, root.val+left+right)
            return root.val+max(left, right)
        dfs(root)
        return maxn