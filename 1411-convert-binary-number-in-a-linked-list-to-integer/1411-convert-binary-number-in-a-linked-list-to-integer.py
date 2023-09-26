# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = [0]
        binary = [1]

        def nextNode(node, res, bin):
            if node.next:
                nextNode(node.next, res, bin)

            if node.val == 1:
                res[0] += bin[0]
                
            bin[0] *= 2

        nextNode(head, result, binary)

        return result[0]
