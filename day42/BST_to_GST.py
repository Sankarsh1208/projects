# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        count = 0
        def rinorder(root):
            nonlocal count
            if not root: return
            if root.right:
                rinorder(root.right)
            count+=root.val
            root.val = count
            if root.left:
                rinorder(root.left)
        rinorder(root)
        return root