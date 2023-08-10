# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def depthNode(node:Optional[TreeNode], count:int) -> int:
            if not node:
                return count
            
            if node.val != None:
                count = count + 1
                
            count = depthNode(node.left, count)
            count = depthNode(node.right, count)
            
            return count
            
        return depthNode(root, 0)
        