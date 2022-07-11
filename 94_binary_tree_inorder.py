# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NodeWrapper:
    def __init__(self, node):
        self.node = node
        self.left_passed = False

class Solution:
    def inorder_rec(self, node, res):
        if node:
            self.inorder_rec(node.left, res)
            res.append(node.val)
            self.inorder_rec(node.right, res)

    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        res = []
        self.inorder_rec(root, res)
        return res

    def inorder_iter(self, root):
        res = []
        if not root:
            return res

        stack = [NodeWrapper(root)]
        while True:
            if len(stack) == 0:
                return res
            
            if stack[-1].node.left and not stack[-1].left_passed:
                stack.append(NodeWrapper(stack[-1].node.left))
                stack[-2].left_passed = True
            elif stack[-1].node.right:
                popped = stack.pop()
                res.append(popped.node.val)
                stack.append(NodeWrapper(popped.node.right))
            else:
                res.append(stack.pop().node.val)

s = Solution()
trees = []
trees.append( TreeNode(1, None, TreeNode(2, TreeNode(3))) )
trees.append( TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))) )
trees.append( TreeNode(6, TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), TreeNode(7)) )
trees.append( TreeNode(6, TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3))), TreeNode(7)) )
for tree in trees:
    print( s.inorder_iter(tree) )
    print( s.inorderTraversal(tree) )



