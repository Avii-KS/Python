class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        self.head = prev

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

# Example usage
n = int(input())
nums = list(map(int, input().split()))

ll = LinkedList()
for num in nums:
    ll.insert_at_end(num)

ll.reverse()
ll.display()
