
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_recur(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            next_node = head.next
            head.next = None
            reversed_list = self.reverseList_recur(next_node)
            next_node.next = head
            return reversed_list
        
### Runtime Complexity: O(n) with n be the length of linked list.