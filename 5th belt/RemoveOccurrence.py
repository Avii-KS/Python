class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def delete_all_occurrences(self, X):
        # Remove all occurrences of X from the linked list
        while self.head and self.head.data == X:  # Handle the head separately
            self.head = self.head.next

        # Traverse the remaining list
        curr = self.head
        while curr and curr.next:
            if curr.next.data == X:
                curr.next = curr.next.next  # Skip the node with value X
            else:
                curr = curr.next  # Move to the next node

    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        print(" ".join(result))

# Input Handling
if __name__ == "__main__":
    n, X = map(int, input().split())  # Number of nodes and value to remove
    values = list(map(int, input().split()))

    ll = LinkedList()
    for value in values:
        ll.insert_at_end(value)

    ll.delete_all_occurrences(X)
    ll.display()
