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
    def create_cycle(self,pos):
        if pos==0:
            return
        curr=self.head
        start_cycle=None
        count=1
        while curr.next:
            if count==pos:
                start_cycle=curr
            curr=curr.next
            count+=1
        curr.next=start_cycle
            
    def has_cycle(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
        
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
            
n=int(input())
arr=list(map(int,input().split()))
pos=int(input())
ll=LinkedList()
for i in arr:
    ll.add(i)
ll.create_cycle(pos)
print("True" if ll.has_cycle() else "False")