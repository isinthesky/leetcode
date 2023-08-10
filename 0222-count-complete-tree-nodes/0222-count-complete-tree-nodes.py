# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        def depthNode(node:Optional[TreeNode], arr:list):
            if not node:
                return
            
            if node.val != None:
                arr[0] += 1
                
            depthNode(node.left, arr)
            depthNode(node.right, arr)
            
        depthNode(root, count)
        
        return count[0]
            
            
        