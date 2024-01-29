def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    previous, current = None, head

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous