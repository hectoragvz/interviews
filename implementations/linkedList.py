# We must implement the basic operations of a linked list
# Append, traverse, and remove


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    def traverseAndPrint(self):
        # We ignore the dummy node
        curr = self.head.next
        while curr:
            print(curr.val, end="-> ")
            curr = curr.next
        print()

    def append(self, val):
        # Since we have a reference to the tail and want to keep it
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            # If this is not met, Index is out of Bounds
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next


list1 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(3)

list1.traverseAndPrint()

list1.remove(2)


list1.traverseAndPrint()
