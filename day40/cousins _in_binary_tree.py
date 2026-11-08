# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        root.val = 0
        if not root.left and not root.right:
            return root
        q = deque([root])
        while q:
            levelsum = 0
            n=len(q)
            for __ in range(n):
                curr = q.popleft()
                if curr.left:
                    levelsum+=curr.left.val
                if curr.right:
                    levelsum+=curr.right.val
                q.append(curr)
            for __ in range(n):
                node = q.popleft()
                sibling = 0
                if node.left:
                    sibling+=node.left.val
                if node.right:
                    sibling+=node.right.val
                
                if node.left:
                    node.left.val = levelsum-sibling
                    q.append(node.left)
                if node.right:
                    node.right.val = levelsum-sibling
                    q.append(node.right)
        return root