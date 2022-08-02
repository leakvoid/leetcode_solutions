class Solution:
    def traverse(self, node, stack, res):
        if not node:
            return
        
        stack.append(str(node.val))
        if not node.left and not node.right:
            r = stack[0]
            for i in range(1, len(stack)):
                r += '->' + stack[i]
            res.append(r)
        
        self.traverse(node.left, stack, res)
        self.traverse(node.right, stack, res)
        stack.pop()
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.traverse(root, [], res)
        return res
