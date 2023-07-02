# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodelist = []

        def treeSearch(node: Optional[TreeNode], arr:list):
            if not node :
                return
            
            treeSearch(node.left, arr)
            treeSearch(node.right, arr)

            if node.val != None:
                arr.append(node.val)

        treeSearch(root, nodelist)

        return nodelist