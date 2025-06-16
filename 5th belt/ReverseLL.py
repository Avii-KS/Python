class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node = Node(data)
            curr.next = new_node
            new_node.prev = curr

    def reverse(self):
        curr = self.head
        prev_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            curr.prev = next_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

# Input and usage
arr = list(map(int, input().split()))
ll = LinkedList()
for i in arr:
    ll.add(i)
ll.reverse()
ll.printlist()