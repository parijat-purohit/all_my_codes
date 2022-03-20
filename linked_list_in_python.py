"""
Linked List implementation in Python
"""
class Node:
    def __init__(self, n):
        self.value = n
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

        
        
        
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# Nodes are created
n1 = Node("Monday")
n2 = Node("Tuesday")
n3 = Node("Wednesday")
n4 = Node("Thursday")
n5 = Node("Friday")
n6 = Node("Saturday")
n7 = Node("Sunday")

# Now link the nodes n1->n2->n3->n4->n5->n6->n7
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

# Finally create a linkedlist object and add n1 nodes address as it's head
ll = LinkedList()
head=ll.head=n1
"""
head or ll.head now contains the address of n1 node. When we reach to n7. n7 nodes next address is
None. We are using this logic to traverse the linked list.
Printing the memory address would give you quite different address what you saw in array before.
"""
print("\nPrinting linked list addresses and values\n")
while(head!=None):
        print(f'Memory Address {head}: , Weekday: {head.value}')
        head = head.next
