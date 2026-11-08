# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        if not root:
            return 0
        ans = [0]
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))
        def dfs(node):
            if not node:
                return -1
            if node.val == start:
                ans[0] = max(ans[0], height(node))
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left != -1:
                ans[0] = max(ans[0], left + 2 + height(node.right))
                return left + 1
            if right != -1:
                ans[0] = max(ans[0], right + 2 + height(node.left))
                return right + 1
            return -1
        dfs(root)
        return ans[0]