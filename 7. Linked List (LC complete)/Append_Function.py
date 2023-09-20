# Odd Even Linked List: Given a Linked List L, separate it into 2 Linked Lists. One contains L's odd nodes and the other contains L's even nodes. For example:

# Input: Head -> 1 -> 2 -> 3 -> 4 -> 5

# Result 1: Head -> 1 -> 3 -> 5
# Result 2: Head -> 2 -> 4

# Note: Odd and Even here refer to the node's position, not value.

# # ----------------------------------------------------------
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

def oddEvenList(head):
    if head == None or head.next == None or head.next.next == None:
        return head
    
    odd = curr = head
    even = evenhead = odd.next
    idx = 1

    while curr:
        if idx > 2 and idx%2 !=0:
            odd.next = curr
            odd = odd.next
        elif idx >2 and idx%2 ==0 :
            even.next = curr
            even = even.next
        curr = curr.next
        idx +=1
    
    even.next = None
    odd.next = evenhead
    
    return head

# Test case
def create_linked_list(values):
    # Helper function to create a linked list from a list of values
    if not values:
        return None

    head = Node(values[0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head



def get_linked_list_values(head):
    # Helper function to get the values of a linked list
    values = []
    curr = head
    while curr:
        values.append(curr.value)
        curr = curr.next
    return values

# Test case
head = create_linked_list([1,2,3,4,5])
result = oddEvenList(head)
result_values = get_linked_list_values(result)
print(result_values)


# ----------------------------------------------------------
                    # WORKING SOLUTION
# ----------------------------------------------------------

# class Node():
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# def oddEvenList(head):
#     if head == None or head.next == None or head.next.next == None:
#         return head
    
#     odd = curr = head
#     even = evenhead = head.next
#     idx = 1

#     while curr:
#         # because we already defined first odd and even, we don't care abt idx 0 and 1
#         if idx > 2 and idx % 2 !=0 :
#             odd.next = curr
#             odd = odd.next
#         elif idx >2 and idx %2 == 0:
#             even.next = curr
#             even = even.next
        
#         curr = curr.next
#         idx += 1
    
#     even.next = None
#     odd.next = evenhead

#     return head


# # Test case
# def create_linked_list(values):
#     # Helper function to create a linked list from a list of values
#     if not values:
#         return None

#     head = Node(values[0])
#     curr = head
#     for value in values[1:]:
#         curr.next = Node(value)
#         curr = curr.next

#     return head


# def get_linked_list_values(head):
#     # Helper function to get the values of a linked list
#     values = []
#     curr = head
#     while curr:
#         values.append(curr.value)
#         curr = curr.next
#     return values

# # Test case
# head = create_linked_list([1,2,3,4,5])
# result = oddEvenList(head)
# result_values = get_linked_list_values(result)
# print(result_values)

