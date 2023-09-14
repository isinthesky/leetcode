# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def depthNodes(node1, node2):
            if not node2:
                return
            
            if node1 and node2:
                node1.val += node2.val

            # if node1 or node2:
            if node1.left:
                depthNodes(node1.left, node2.left if node2 else None)
            elif node2.left and not node1.left:
                node1.left = node2.left
                depthNodes(node1.left, None)

            if node1.right:
                depthNodes(node1.right, node2.right if node2 else None)
            elif node2.right and not node1.right:
                node1.right = node2.right
                depthNodes(node1.right, None)

        if not root2:
            return root1
        
        if not root1:
            return root2

        depthNodes(root1, root2)

        return root1