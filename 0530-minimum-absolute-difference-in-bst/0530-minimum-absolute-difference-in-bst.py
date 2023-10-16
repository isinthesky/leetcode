# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = [999999]
        arr = []

        def depthNode(node, res):
            arr.append(node.val)   

            if node.left:
                depthNode(node.left, res)

            if node.right:
                depthNode(node.right, res)

        depthNode(root, arr)
        arr.sort()

        for pos in range(len(arr)-1):
            gap = arr[pos+1] - arr[pos]

            if result[0] > gap:
                result[0] = gap

        return result[0]
