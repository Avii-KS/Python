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
            
    def sortlist(self):
        count=[0,0,0]
        curr=self.head
        
        while curr:
            count[curr.data]+=1
            curr=curr.next
            
        curr=self.head
            
        for i in range(3):
            while count[i]>0:
                curr.data=i
                curr=curr.next
                count[i]-=1
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
            
n=int(input())
arr=list(map(int,input().split()))
ll=LinkedList()
for i in arr:
    ll.add(i)
ll.sortlist()
ll.display()