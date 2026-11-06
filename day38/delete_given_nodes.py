# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        q = []
        res = []
        if not root:
            return []
        deleted = set(to_delete)
        if root.val not in deleted:
            res.append(root)
        q.append((root, None, False))
        while q:
            node, parent, left = q.pop(0)
            if node.left:
                q.append((node.left, node, True))
            if node.right:
                q.append((node.right, node, False))
            if node.val in deleted:
                if parent:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                if node.left and node.left.val not in deleted:
                    res.append(node.left)
                if node.right and node.right.val not in deleted:
                    res.append(node.right)
        return res