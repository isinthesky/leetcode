# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def depthNode(node: Optional[TreeNode], rem:str, arr:list):
            preStr = ""
            if rem != "":
                preStr = rem+"->"

            if not node.left and not node.right:
                arr.append(preStr + str(node.val))

            if node.left:
                depthNode(node.left, preStr + str(node.val), arr)
                
            if node.right:
                depthNode(node.right, preStr + str(node.val), arr)

        treeWay = []
        depthNode(root, "", treeWay)

        return treeWay
            