# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        pin = len(inorder) - 1
        def build(s, e):
            nonlocal pin
            if s>e: return None
            root = TreeNode(postorder[pin])
            pin-=1
            root.right = build(inorder.index(root.val) + 1, e)
            root.left = build(s, inorder.index(root.val) - 1)
            return root
        return build(0, len(inorder)-1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        j = len(inorder)-1
        for i in range(len(postorder)-2, -1, -1):
            node = stack[-1]
            if node.val != inorder[j]:
                node.right = TreeNode(postorder[i])
                stack.append(node.right)
            else:
                while stack and stack[-1].val==inorder[j]:
                    node = stack.pop()
                    j-=1
                node.left = TreeNode(postorder[i])
                stack.append(node.left)
        return root
