# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(root):
            if not root:
                return 0, None
            ld, llca = dfs(root.left)
            rd, rlca = dfs(root.right)
            if ld>rd:
                return ld+1, llca
            if rd>ld:
                return rd+1, rlca
            return rd+1, root
        return dfs(root)[1]