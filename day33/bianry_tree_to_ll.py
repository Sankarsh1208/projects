#my solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        stack = []
        def preorder(root):
            if not root:
                return None
            stack.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        for i in range(len(stack)-1):
            stack[i].left = None
            stack[i].right = stack[i+1]
        stack[-1].left = None
        stack[-1].right = None

#learned solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def build(root):
            if not root:
                return
            left = build(root.left)
            right = build(root.right)
            if root.left:
                left.right = root.right
                root.right = root.left
                root.left = None
            return right or left or root
        build(root)
