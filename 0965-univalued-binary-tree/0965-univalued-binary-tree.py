# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        result = [True]

        def depthNode(node, value, res)-> bool:
            if node.val != value:
                res[0] = False

            if node.left:
                depthNode(node.left, value, res)
            
            if node.right:
                depthNode(node.right, value, res)

        depthNode(root, root.val, result)

        return result[0]
