# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        
        def bfs(node, depth, res):
            if node:
                depth += 1

                if len(res) <= depth:
                    res.append([node.val])
                else:
                    res[depth].append(node.val)

                if node.left:
                    bfs(node.left, depth, res)

                if node.right:
                    bfs(node.right, depth, res)

        bfs(root, -1, result)

        return result
