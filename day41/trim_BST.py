# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        def newroot(root):
            if not root:
                return None
            if root.val>high:
                return newroot(root.left)
            if root.val<low:
                return newroot(root.right)
            root.left = newroot(root.left)
            root.right = newroot(root.right)
            return root
        return newroot(root)
        