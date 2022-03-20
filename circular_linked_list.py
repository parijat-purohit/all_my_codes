"""
Circular Linked List implementation in Python
"""
class Node:
    def __init__(self, n):
        self.value = n
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None



# Nodes are created
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)


# Now link the nodes in a circular fashion n1->n2->n3->n1  
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1


# Finally create a linkedlist object and add n1 nodes address as it's head
ll = LinkedList()
start=ll.head=n1
# print the first node to avoid cycle
print("\nPrinting linked list addresses and values\n")
print(f'Memory Address {ll.head}: , number: {ll.head.value}')

head = start.next
"""
head now contains the address of n2 node. When we reach to n4. n4 node's next address is
n1. 
"""
while(head!=start):
        print(f'Memory Address {head}: , number: {head.value}')
        head = head.next
# print the last value (it's a cycle so it's actually the first value :))
print(f'Memory Address {head}: , number: {head.value}')
