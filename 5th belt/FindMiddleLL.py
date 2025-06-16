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
        Node(data).prev = curr
    
    def findMiddle(self):
        fast = self.head
        slow = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)
    
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
arr = list(map(int, input().split()))
ll = Linkedlist()
for i in arr:
    ll.add(i)
ll.findMiddle()