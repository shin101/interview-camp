# Odd Even Linked List: Given a Linked List L, separate it into 2 Linked Lists. One contains L's odd nodes and the other contains L's even nodes. For example:

# Input: Head -> 1 -> 2 -> 3 -> 4 -> 5

# Result 1: Head -> 1 -> 3 -> 5
# Result 2: Head -> 2 -> 4

# Note: Odd and Even here refer to the node's position, not value.

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

def getOddEven(head):
    counter = 1
    if head == None:
        return;
    while head:
        if counter%2 ==0:
            head.next = head
        else:
            head.next = head
        head = head.next
        counter += 1
    return head

ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)

# call getOddEven function and print the results
print(getOddEven(ll))

# should return : Result 1: 1 3 5
# Result 2 : 2 4
