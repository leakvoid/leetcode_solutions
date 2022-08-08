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
        if root == None:
            return str([None]).replace(" ", "")
        
        unrolled = [root]
        start = 0
        end = 1
        next_pass = True
        
        while next_pass:
            next_pass = False
            for i in range(start, end):
                if unrolled[i]:
                    next_pass = True
                    unrolled.append( unrolled[i].left )
                    unrolled.append( unrolled[i].right )
            start = end
            end = len(unrolled)
                    
        for i in range(len(unrolled) - 1, -1, -1):
            if unrolled[i]:
                break
            unrolled.pop()
            
        res = []
        for i in range(len(unrolled)):
            if unrolled[i]:
                res.append( unrolled[i].val )
            else:
                res.append( None )
        
        return str(res).replace(" ", "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        if data[0] == 'None':
            return None
        data = list(map(lambda x: None if x == 'None' else int(x), data))
        if len(data) % 2 == 0:
            data.append(None)
        
        unrolled = [ TreeNode(data[0]) ]
        end = 1
        node_count = 1
        
        last_tree_pos = 0
        i = 1
        while i < len(data):
            end = min(end + node_count * 2, len(data))
            node_count = 0

            while i < end:
                if data[i] != None:
                    unrolled[last_tree_pos].left = TreeNode( data[i] )
                    unrolled.append( unrolled[last_tree_pos].left )
                    node_count += 1
                
                if data[i+1] != None:
                    unrolled[last_tree_pos].right = TreeNode( data[i+1] )
                    unrolled.append( unrolled[last_tree_pos].right )
                    node_count += 1
                
                last_tree_pos += 1
                i += 2
        
        return unrolled[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
