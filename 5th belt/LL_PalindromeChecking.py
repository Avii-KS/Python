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
    def palindrome(self):
        values=[]
        curr=self.head
        while curr:
            values.append(curr.data)
            curr=curr.next
        return values==values[::-1]
        
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
            
n=int(input())
if n=="0":
    print("True")
else:
    arr=list(map(int,input().split()))
    ll=LinkedList()
    for i in arr:
        ll.add(i)
    print(ll.palindrome())
    # ll.display()