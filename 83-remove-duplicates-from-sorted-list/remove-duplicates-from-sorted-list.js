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
var deleteDuplicates = function(head) {
    if(head == null) return null
    let current = head
    let prev = head
    while(current != undefined){
        console.log(current.val,prev.val)
        if(current.val !== prev.val) {
            console.log(current.val, prev.val)
            prev.next = current
            prev = current
        }
        current = current.next
    }
    prev.next = null
    return head
};