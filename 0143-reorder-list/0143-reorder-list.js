/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    
    if (!head)
        return;
    
    if (!head.next)
        return head;
    
    const stack = []
    let node = head
    length = 0

    while(node) {
        stack.push(node)
        node = node.next
        length += 1
    }

    node = head
        
    console.log(length, stack, Math.floor(stack.length/2))

    
    
    for (let i = 0; i < Math.floor(length/2); i += 1)
    {
        console.log(i)
        getNode = stack.pop();
        console.log(11)
        nextNode = node.next;
        console.log(22)

        node.next = getNode;
        console.log(33)
        getNode.next = nextNode;
        console.log(44)
        node = nextNode;
        console.log(55)
    }
    
    // if node.next
    if (length % 2 > 0) {
        node.next = null
    } else {
        node.next.next = null
    }

};