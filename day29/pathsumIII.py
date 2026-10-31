# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, target: int) -> int:
        ans = 0
        temp = defaultdict(int)
        temp[0] = 1
        def dfs(node, pre):
            nonlocal ans
            if not node:
                return
            pre += node.val
            ans += temp[pre-target]
            temp[pre] += 1
            dfs(node.left, pre)
            dfs(node.right, pre)
            temp[pre] -= 1
            pre -= node.val
        dfs(root, 0)
        return ans