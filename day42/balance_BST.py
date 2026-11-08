# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        def build(left, right):
            if left>right:
                return None
            mid = (left+right)//2
            node = TreeNode(arr[mid])
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node
        inorder(root)
        return build(0, len(arr)-1)