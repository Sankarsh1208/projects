# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]: 
        res = []
        def zigzag(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            
            zigzag(root.left, depth+1)
            zigzag(root.right, depth+1)

        zigzag(root, 0)
        for depth in range(1, len(res), 2):
            res[depth].reverse()
        return res