class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    p1 = list1
    p2 = list2
    curr = dummy

    while p1 and p2:
        if p1.val > p2.val:
            curr.next = p2
            p2 = p2.next
        else:
            curr.next = p1
            p1 = p1.next
        curr = curr.next

    if p1:
        curr.next = p1
    if p2:
        curr.next = p2

    return dummy.next
