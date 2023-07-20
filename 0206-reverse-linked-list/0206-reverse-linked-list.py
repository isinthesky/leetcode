# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = deque()

        def depth(node, que):
            if node:
                if node.next:
                    que.append(node.val)
                    depth(node.next, que)
                    node.val = que.popleft()
                else:
                    que.append(node.val)
                    node.val = que.popleft()
        
        depth(head, res)

        return head
