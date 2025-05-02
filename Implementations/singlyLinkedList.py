class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = LinkNode(1)
        self.tail = self.head

    def append(self, val):
        node = LinkNode(val)
        self.tail.next = node
        self.tail = self.tail.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print()

    def count(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def delete(self, pos):
        i = 0
        curr = self.head
        while i < pos and curr:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next


ll = LinkList()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()
ll.remove(3)
ll.print()
