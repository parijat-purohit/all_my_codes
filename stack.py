"""
stack implementation in Python
"""
class Node:
    def __init__(self, n):
        self.value = n
        self.next = None

class Stack: #LIFO fashion
    def __init__(self):
        self.head=None
    def push(self, node):
        # Is it the first item to be pushed. No worries. Just add the node in it's head
        if self.head == None:
            self.head = node
        # If there exists items before, make sure to push the new item and point it to previous head
        else:
            temp = self.head
            self.head = node
            self.head.next= temp

    def pop(self):
        if self.head==None:
            print("No item to pop")
        else:
            temp = self.head.next
            self.head = None
            self.head = temp
        
# Nodes are created
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)


# Finally create a stack object and push the first node
s = Stack()
"""
Play with this test cases by uncommenting one by one and running it
"""
# s.push(n1) 
# s.push(n2)
# s.pop()
# s.push(n3)
# s.push(n4)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
while(s.head!=None):
    print(s.head.value)
    s.head = s.head.next
