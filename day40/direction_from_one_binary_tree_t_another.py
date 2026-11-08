# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def find(root, val, s):
            if not root:
                return False
            if root.val == val:
                return True
            if root.left and find(root.left, val, s):
                s.append('L')
                return True
            if root.right and find(root.right, val, s):
                s.append('R')
                return True
            return False
        s = []
        e = []
        find(root, startValue, s)
        find(root, destValue, e)
        s.reverse()
        e.reverse()
        i=0
        while i < min(len(s), len(e)) and s[i] == e[i]:
            i += 1
        return 'U' * (len(s) - i) + ''.join(e[i:])