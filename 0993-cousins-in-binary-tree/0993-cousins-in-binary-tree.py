# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dest = [x, y]
        parent = 0
        dep = 1
                
        def depthNode(node, value, depth, arr):
            if node.left:
                if node.left.val in value:
                    arr.append([node.val, depth])
                    return
                else:
                    depthNode(node.left, value, depth + 1, arr)
                
            if node.right:
                if node.right.val in value:
                    arr.append([node.val, depth])
                    return
                else:
                    depthNode(node.right, value, depth + 1, arr)

        resArray = []
        depthNode(root, dest, 0, resArray)

        if 2 == len(resArray):
            if resArray[0][parent] ==  resArray[1][parent]:
                return False

            return True if resArray[0][dep] == resArray[1][dep] else False
        
        return False
        