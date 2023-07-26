# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper( node ):
            # Base case: empty node, or only one node
            if not node or not node.next:
                return node

            # General case:
            next_node = node.next
            next_pair = next_node.next

            # Reverse next node linkage
            next_node.next = node

            # Update node linkage to next pair
            node.next = helper( next_pair)

            # return new head after swap
            return next_node        
        # ------------------------------

        return helper( head )
        