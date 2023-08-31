# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        nodeDict = {}

        def dfs(node, dic):
            if node :
                if node.val in dic:
                    dic[node.val] += 1
                else:
                    dic[node.val] = 1

                dfs(node.left, dic)
                dfs(node.right, dic)

        dfs(root,nodeDict)

        bigValue = 0
        resSet = set()

        for k, v in nodeDict.items():
            if v > bigValue:
                resSet.clear()
                bigValue = v
                resSet.add(k)
            if v == bigValue:
                resSet.add(k)
            
        return list(resSet)
        