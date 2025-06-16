class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, value):
        new_node = Node(value)

        # If inserting at the head (position 0)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        # Traverse to find the position
        curr = self.head
        for _ in range(position - 1):
            if not curr:
                return  # Invalid position
            curr = curr.next

        # Insert the node at the specified position
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def create_from_list(self, values):
        for value in values:
            self.insert_at_end(value)

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

# Input handling and execution
if __name__ == "__main__":
    n, k, val = map(int, input().split())  # Read n, k, and val
    if n > 0:
        values = list(map(int, input().split()))  # Read the doubly linked list elements
    else:
        values = []

    dll = DoublyLinkedList()
    dll.create_from_list(values)

    # Print the original doubly linked list
    original = dll.display()
    print(" ".join(map(str, original)))

    # Insert the node at position k
    dll.insert_at_position(k, val)

    # Print the modified doubly linked list
    modified = dll.display()
    print(" ".join(map(str, modified)))
