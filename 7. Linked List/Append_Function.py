# Odd Even Linked List: Given a Linked List L, separate it into 2 Linked Lists. One contains L's odd nodes and the other contains L's even nodes. For example:

# Input: Head -> 1 -> 2 -> 3 -> 4 -> 5

# Result 1: Head -> 1 -> 3 -> 5
# Result 2: Head -> 2 -> 4

# Note: Odd and Even here refer to the node's position, not value.


# class Node():
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# def getOddEven(head):
#     if not head:
#         return head
#     odd_pointer = current = head
#     even_pointer = head.next
#     idx = 1

#     while current:
#         if idx > 2 and idx % 2 != 0:
#             odd_pointer.next = current
#             odd_pointer = odd_pointer.next
#         elif idx > 2 and idx % 2 == 0:
#             even_pointer.next = current
#             even_pointer = even_pointer.next

#         current = current.next
#         idx+=1
    
#     even_pointer.next = None
#     odd_pointer
#     return head



    

# ll = Node(1)
# ll.next = Node(2)
# ll.next.next = Node(3)
# ll.next.next.next = Node(4)
# ll.next.next.next.next = Node(5)

# # call getOddEven function and print the results
# print(getOddEven(ll))

# should return : Result 1: 1 3 5
# Result 2 : 2 4



