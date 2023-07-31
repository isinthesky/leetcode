# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        stack = []
        node = head
        
        while node:
            stack.append(node)
            node = node.next
        
        node = head
        
        for i in range(len(stack)//2):
            getNode = stack.pop()
            nextNode = node.next
            node.next = getNode
            getNode.next = nextNode
            node = nextNode
        
        node.next = None    
