# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head :
            return False

        slow = head
        fast = head.next
        pos = -1

        while slow != fast :

            # print(slow.val, fast.val)
            if not fast or not fast.next :
                return False
            slow = slow.next
            pos += 1

            fast = fast.next.next

        print(pos)
        return True
            

