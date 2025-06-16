class Node:

  def __init__(self,data):
    self.data=data
    self.next=None

def traverse(head):

  if head is None:
    print()
    return
  
  print(head.data,end=" ")

  traverse(head.next)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

traverse(head)

    