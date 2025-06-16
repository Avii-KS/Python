class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def remove_nth_from_end(self, n):
        # Create a dummy node to simplify edge cases (e.g., removing the head)
        dummy = Node(0)
        dummy.next = self.head
        first = second = dummy

        # Move `first` n + 1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until `first` reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Update head in case the first node was removed
        self.head = dummy.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("nullptr")

# Input handling
n = int(input())  # Number of elements in the list
elements = list(map(int, input().split()))  # Linked list elements
k = int(input())  # Position from the end to remove

# Create and populate the linked list
ll = LinkedList()
for el in elements:
    ll.add(el)

# Remove the kth node from the end
ll.remove_nth_from_end(k)

# Display the resulting linked list
ll.display()