# Implementing a Linked List from Scratch


class LinkedList:
    def __init__(self):
        self.head = ListNode(1)
        self.tail = self.head


# Create a ListNode class
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode("red")
node2 = ListNode("blue")
node3 = ListNode("green")

linklist = LinkedList()
linklist.head = node1

print(linklist.head.val)
