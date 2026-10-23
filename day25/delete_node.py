# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def deln(root, key):
            if not root:
                return
            if root.val>key:
                root.left = deln(root.left, key)
            elif root.val<key:
                root.right = deln(root.right, key)
            else:
                if root.left is None and root.right is None:
                    return
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    temp = getrightmin(root.right)
                    root.val = temp.val
                    root.right = deln(root.right, temp.val)

            return root
        def getrightmin(r):
            temp = r
            while temp.left:
                temp = temp.left
            return temp
        return deln(root,key)