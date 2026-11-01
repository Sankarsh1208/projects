# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        res = []
        d = defaultdict(int)
        def dfs(root):
            if not root:
                return '#'
            temp = (root.val, dfs(root.left), dfs(root.right))
            d[temp]+=1
            if d[temp]==2:
                res.append(root)
            return temp
        dfs(root)
        return res