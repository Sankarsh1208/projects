# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def build(root, count):
            if not root:
                return 0 
            count = count*10 + root.val
            if not root.left and not root.right:
                return count
            
            return build(root.left, count) + build(root.right, count)
        return build(root, 0)
        