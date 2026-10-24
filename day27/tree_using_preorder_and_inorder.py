# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        inorder_index = 0
        for val in preorder[1:]:
            node = TreeNode(val)
            if stack[-1].val != inorder[inorder_index]:
                stack[-1].left = node
                stack.append(node)
            else:
                last_popped = None
                while (stack and inorder_index < len(inorder) 
                    and stack[-1].val == inorder[inorder_index]):
                    last_popped = stack.pop()
                    inorder_index += 1
                last_popped.right = node
                stack.append(node)

        return root