class Node:
    def __init__(self) -> None:
        self.val = None
        self.next = None
    
def reverse(head):
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp.val)
        temp = temp.next
        

def display(head):
    while head is not None:
        print(f"{head.val}", end = " ")
        head = head.next
    print()
head = Node(1)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next  =Node(5)
print("original linkedlist", display(head))
print("reversed linkedlist", reverse(head))
