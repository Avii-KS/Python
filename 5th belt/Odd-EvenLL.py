class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            new_node=Node(data)
            curr.next=new_node
    def group(self):
        if not self.head or not self.head.next:
            return
        
        odd=self.head
        even=self.head.next
        even_head=even
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
            
        odd.next=even_head
        
    def printlist(self):
        if not self.head:
            print("No elements")
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        
            
n=int(input())
if n==0:
    print("No elements")
else:
    arr=list(map(int,input().split()))
    ll=LinkedList()
    for i in arr:
        ll.add(i)
    ll.group()
    ll.printlist()
    