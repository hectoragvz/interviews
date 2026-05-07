# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = head

        while n > 0:
            second = second.next
            n -= 1

        while second:
            second = second.next
            first = first.next

        # We now have the node to delete at first.next
        first.next = first.next.next
        return dummy.next
