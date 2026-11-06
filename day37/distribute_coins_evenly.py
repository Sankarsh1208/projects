# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    moves = 0
    def distributeCoins(self, root: TreeNode | None) -> int:
        def dfs(root, parent):
            if not root: return 0
            self.moves = dfs(root.left, root)+dfs(root.right, root)
            x = root.val-1
            if parent:
                parent.val+=x
            self.moves+=abs(x)
            return self.moves
        return dfs(root, None)