# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        s = []
        q = deque([root])
        while q:
            temp = q.popleft()
            if temp is None:
                s.append('#')
                continue
            s.append(str(temp.val))
            q.append(temp.left)
            q.append(temp.right)
        return ",".join(s)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
    
        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return []
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        while q and i<len(values):
            node = q.popleft()
            
            if values[i]!='#':
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i+=1
            
            if values[i]!='#' and i<len(values):
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))