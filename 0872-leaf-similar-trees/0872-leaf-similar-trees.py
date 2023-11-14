# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def depthNode(node, arr):
            if node.left:
                depthNode(node.left, arr)
            
            if node.right:
                depthNode(node.right, arr)

            if not node.left and not node.right:
                arr.append(node.val)

        leafList1 = []
        leafList2 = []

        depthNode(root1, leafList1)
        depthNode(root2, leafList2)

        return True if leafList1 == leafList2 else False
