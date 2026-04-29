def reverseList(head):
    dummy = None
    curr = head

    while curr:
        res = curr.next
        curr.next = dummy
        dummy = curr
        curr = res

    return dummy
