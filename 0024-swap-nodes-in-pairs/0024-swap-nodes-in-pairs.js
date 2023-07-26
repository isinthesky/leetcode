/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const helper = (node) => {
        if (!node || !node.next) {
            return node
        }

        const next_node = node.next;
        const next_pair = next_node.next;

        next_node.next = node

        node.next = helper(next_pair)
        return next_node
    }

    return helper (head)
};


    // def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    //     def helper( node ):
    //         # Base case: empty node, or only one node
    //         if not node or not node.next:
    //             return node

    //         # General case:
    //         next_node = node.next
    //         next_pair = next_node.next

    //         # Reverse next node linkage
    //         next_node.next = node

    //         # Update node linkage to next pair
    //         node.next = helper( next_pair)

    //         # return new head after swap
    //         return next_node        
    //     # ------------------------------

    //     return helper( head )
        