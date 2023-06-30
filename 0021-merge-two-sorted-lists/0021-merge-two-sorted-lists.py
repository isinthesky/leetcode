# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        if not list1:
            return list2
        if not list2:
            return list1

        cur = dummy = ListNode()

        if list1.val <= list2.val:
            dummy.val = list1.val
            list1 = list1.next
        else:
            dummy.val = list2.val
            list2 = list2.next

        while list1 and list2 :
            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy
                