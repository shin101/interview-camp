# Is Palindrome: Given a Linked List, determine if it is a Palindrome.
# For example, the following lists are palindromes:A -> B -> C -> B -> A
# A -> B -> B -> A
# K -> A -> Y -> A -> K
# Note​: Do it with O(N) time and O(1) space (Hint: Reverse a part of the list)


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def isPalindrome(head):
    pass


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('C')
e = Node('B')
f = Node('A')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

g = Node('A')
h = Node('B')
i = Node('C')
j = Node('C')
k = Node('A')
g.next = h
h.next = i
i.next = j
j.next = k

print(isPalindrome(a)) # Expected output: True
print(isPalindrome(g)) # Expected output: False



# =============== WORKING SOLUTION ===============

# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def isPalindrome(head):
#     fast = head
#     slow = head

#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next

#     prev = None
#     while slow: 
#         temp = slow.next
#         slow.next = prev
#         prev = slow 
#         slow = temp 
    
#     left, right = head, prev
#     while right:
#         if left.value != right.value:
#             return False
#         left = left.next
#         right = right.next
#     return True