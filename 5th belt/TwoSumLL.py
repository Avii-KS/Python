class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
    
    def twosum(self, target):
        seen = set()
        curr = self.head
        found = False
        while curr:
            complement = target - curr.data
            if complement in seen:
                print(min(curr.data, complement), max(curr.data, complement))
                found = True
            seen.add(curr.data)
            curr = curr.next
        if not found:
            print(-1)
            
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
ll = LinkedList()
for i in arr:
    ll.add(i)
ll.twosum(target)