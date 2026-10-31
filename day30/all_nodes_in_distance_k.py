# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        res = []
        d = defaultdict(list)
        def find_parent(root):
            if not root:
                return
            if root.left:
                d[root.left]=root
            if root.right:
                d[root.right]=root
            find_parent(root.left)
            find_parent(root.right)
        find_parent(root)
        visited = {target}
        res = []
        q = deque([(target, 0)])
        while q:
            top, dist = q.popleft()
            if dist == k:
                res.append(top.val)
                continue
            for node in (top.left, top.right, d.get(top)):
                if node and node not in visited:
                    visited.add(node)
                    q.append((node, dist+1))
        return res