# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            if list2 is None:
                return None
            else:
                return list2
        else:
            if list2 is None:
                return list1
            else:
                if list1.val <= list2.val:
                    return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
                else:
                    return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))

