# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = set()

        while headA :
            dic.add(headA)
            headA = headA.next

        while headB :
            if headB in dic:
                for aa in dic:
                    if headB == aa :
                        return headB

            headB = headB.next

            
        
        return None