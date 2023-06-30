# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head :
            node = head

            while node.next :
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next

        return head