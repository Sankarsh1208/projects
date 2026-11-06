# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.f = self.s = self.p = None
        def inorder(root):
            if not root: 
                return
            inorder(root.left)
            if self.p and self.p.val>root.val:
                if not self.f:
                    self.f = self.p
                self.s = root
            self.p = root
            inorder(root.right)
        inorder(root)
        self.f.val, self.s.val = self.s.val, self.f.val