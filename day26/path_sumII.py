# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        def path(r, rem, ans):
            if r is None:
                return
            ans.append(r.val) 
            if not r.left and not r.right:
                if r.val==rem:
                    res.append(ans.copy())
            
            else:
                rem-= r.val
                path(r.left, rem, ans)
                path(r.right, rem, ans)
            ans.pop()
        ans = []
        path(root, targetSum, ans)
        return res