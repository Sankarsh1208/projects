# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q = deque([root])
        maxv = float('-inf')
        maxl = 0
        level = 1
        while q:
            n = len(q)
            sumn = 0
            for _ in range(n):
                node = q.popleft()
                sumn+=node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxv<sumn:
                maxv = sumn
                maxl = level
            level+=1
        return maxl