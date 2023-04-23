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
    if not head:
        return False

    slow = head
    fast = head

    # determine mid point
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of LL
    prev = None
    curr = slow.next 
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    slow.next = prev

    # Compare the first and second half of the linked list
    first_half = head
    second_half = slow.next
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True

    

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

print(isPalindrome(a)) # Expected output: True