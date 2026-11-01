# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def sear(root, low, high):
            if not root: 
                return True
            if root.val<=low or root.val>=high: 
                return False
            return sear(root.left, low, root.val) and sear(root.right, root.val, high)
        return sear(root, float('-inf'), float('inf'))