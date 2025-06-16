class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def delete(head):
    return head.next if head else None
    
def printlist(head):
    while head:
        print(head.data,end=" ")
        head=head.next
            
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)

delete_head=delete(head)
printlist(delete_head)