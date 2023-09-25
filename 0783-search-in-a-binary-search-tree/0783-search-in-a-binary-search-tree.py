# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result = TreeNode(val=-1)

        def depthNode(node, val, res):
            if node.val == val:
                res.val = val
                res.left = node.left
                res.right = node.right
            else:
                if node.left:
                    depthNode(node.left, val, res)
                if node.right:
                    depthNode(node.right, val, res)

        depthNode(root, val, result)

        return None if result.val < 0 else result
        