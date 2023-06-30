# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        node = head
        mem = None

        arr = []

        pos = 0 
        def compArr(cnode: Optional[ListNode]) -> bool:
            temp = set()
            while cnode:
                if cnode in temp:
                    return True
                temp.add(cnode)
                cnode = cnode.next

            return False

        while node :
            if node.val in arr:
                pos = arr.index(node.val)

                if compArr(node) == True:
                    return True
                else:
                    return False

            else:
                arr.append(node.val)
                node = node.next

    

        pos = -1
        return False
        
        