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
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # def to_list(self):
    #     """Convert the linked list to a Python list."""
    #     result = []
    #     current = self.head
    #     while current:
    #         result.append(current.data)
    #         current = current.next
    #     return result

    # def from_list(self, sorted_list):
    #     """Convert a sorted Python list back to a linked list."""
    #     self.head = None
    #     for data in sorted_list:
    #         self.add(data)

    # def sort(self):
    #     """Sort the linked list."""
    #     # Convert linked list to a Python list
    #     elements = self.to_list()
    #     # Sort the list
    #     elements.sort()
    #     # Convert back to linked list
    #     self.from_list(elements)
    def print_list(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
def merge_two_sorted_lists(list1, list2):
    """Merge two sorted linked lists into a single sorted linked list."""
    merged_list = LinkedList()  # Initialize an empty LinkedList
    current1 = list1.head
    current2 = list2.head
    
    while current1 and current2:
        if current1.data < current2.data:
            merged_list.add(current1.data)
            current1 = current1.next
        else:
            merged_list.add(current2.data)
            current2 = current2.next

    while current1:
        merged_list.add(current1.data)
        current1 = current1.next

    while current2:
        merged_list.add(current2.data)
        current2 = current2.next

    return merged_list

# Input
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
list1 = LinkedList()
for i in arr1:
    list1.add(i)
list2 = LinkedList()
for i in arr2:
    list2.add(i)

# Create linked list
merged_list = merge_two_sorted_lists(list1, list2)

# Sort the linked list
# ll.sort()

# Print the sorted linked list
merged_list.print_list()
