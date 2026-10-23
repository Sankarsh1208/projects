#using arrays:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = []
        def search(r):
            if r is None:
                return 
            search(r.left)
            res.append(r.val)
            search(r.right)
        search(root)
        return res[k-1]

#without storage:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def search(r, a, k):
            if r is None:
                return 0
            ans = search(r.left, a, k)
            if ans!=0:
                return ans
            a[0]+=1
            if a[0]==k:
                return r.val
            return search(r.right, a, k)
        a = [0]
        return search(root, a, k)
        