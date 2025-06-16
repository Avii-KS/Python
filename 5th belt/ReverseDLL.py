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
        prev = None
        while curr:
            # Swap next and prev for the current node
            curr.next, curr.prev = curr.prev, curr.next
            prev = curr  # Update prev to the current node
            curr = curr.prev  # Move to the previous node (which is the next in the original list)
        self.head = prev  # Update the head to the new front
        
    def printlist(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next  # Traverse in forward order after reversal
        print(" ".join(map(str, result)))

# Input handling
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # List elements

ll = LinkedList()
for i in arr:
    ll.add(i)

ll.reverse()  # Reverse the doubly linked list
ll.printlist()  # Print the reversed list