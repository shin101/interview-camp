# Given a Linked List with a cycle, find the node where the cycle begins. Do it in O(1) memory

# HINT
    # find length of the cycle
    # advance fast pointer by that length
    # advance fast and slow pointers by 1 til they meet
    # where they meet is the start of the cycle 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def findCycleStart(head):
    if not head : return
    slow, fast = head, head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            break

    new_head = head

    while fast!=new_head:
        new_head = new_head.next
        fast = fast.next

    return new_head

    

# Test case
if __name__ == "__main__":
    # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle starts at 3)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next  # Creating a cycle here

    # Find the start of the cycle
    cycle_start_node = findCycleStart(head)

    # Expected output: The value of the node where the cycle begins is 3
    if cycle_start_node:
        print("The value of the node where the cycle begins is:", cycle_start_node.value)
    else:
        print("There is no cycle in the linked list.")



# ----------------------------working solution---------------------------


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def findCycleStart(head):
#     if not head: return

#     slow, fast = head, head
#     while fast.next and fast.next.next:
#         slow = slow.next
#         fast = fast.next.next
#         if fast == slow: break
    
#     if not fast.next or not fast.next.next: return None

#     pointer = head

#     while pointer != fast:
#         pointer = pointer.next
#         fast = fast.next

#     return pointer

# if __name__ == "__main__":
#     # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle starts at 3)
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head.next.next.next.next.next = head.next.next  # Creating a cycle here

#     # Find the start of the cycle
#     cycle_start_node = findCycleStart(head)

#     # Expected output: The value of the node where the cycle begins is 3
#     if cycle_start_node:
#         print("The value of the node where the cycle begins is:", cycle_start_node.value)
#     else:
#         print("There is no cycle in the linked list.")