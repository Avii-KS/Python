class Node:

  def __init__(self,data):
    self.data = data
    self.next=None

def search(head,key):

  if head is None:
    return False
  
  if head.data==key:
    return True
  
  return search(head.next,key)

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

key=50

if search(head,key):
  print("Yes")
else:
  print("No")