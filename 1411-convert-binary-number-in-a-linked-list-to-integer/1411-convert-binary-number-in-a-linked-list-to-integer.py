# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = [0]

        def nextNode(node, res):
            if node.next:
                ret = nextNode(node.next, res)
                if node.val == 1:
                   res[0] += ret
                return ret * 2
            else:
                if node.val == 1:
                    res[0] += 1
                return 2

        nextNode(head, result)

        return result[0]
