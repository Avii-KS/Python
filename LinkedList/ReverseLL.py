class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    
    if head is None or head.next is None:
        return head
        
    rev=reverse(head.next)
    
    head.next.next=head
    head.next=None
    
    return rev
    
def printlist(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.next
    print()
        
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)

reverse_head=reverse(head)
printlist(reverse_head)