class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
        
    
    def sortList(self):
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr and curr.next:
                if curr.data > curr.next.data:  # Swap values if needed
                    curr.data, curr.next.data=curr.next.data, curr.data
                    swapped = True
                curr = curr.next  # Move to the next node
    
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
arr = list(map(int, input().split()))
ll = Linkedlist()
for i in arr:
    ll.add(i)
ll.sortList()
ll.printList()