# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        resStr = str(root.val)

        def depthNode(node: Optional[TreeNode]) -> str:
            temp = "(" + str(node.val)

            if node.left:
                temp += depthNode(node.left)

            if node.right:
                if not node.left:
                    temp += "()"
                temp += depthNode(node.right)

            temp += ")"

            return temp

        if root.left:
            tempstr = depthNode(root.left)
            print("left", tempstr)
            resStr += tempstr

        if root.right:
            if not root.left:
                resStr += "()"
            tempstr = depthNode(root.right)
            print("right", tempstr)
            resStr += tempstr

        return resStr
            