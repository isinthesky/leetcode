# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodelist = []

        def treeSearch(node: Optional[TreeNode], arr:list):
            if not node :
                return
            
            if node.val != None:
                arr.append(node.val)
            
            if node.left :
                treeSearch(node.left, arr)

            if node.right :
                treeSearch(node.right, arr)

        treeSearch(root, nodelist)

        return nodelist
