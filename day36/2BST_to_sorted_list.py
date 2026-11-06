# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        res1 = []
        res2 = []
        def inorder(root, res):
            if not root: return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        inorder(root1, res1)
        inorder(root2, res2)
        return sorted(res1+res2)