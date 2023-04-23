# Given a Linked List with a cycle, find the node where the cycle begins.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def findCycleStart(head):
    # find length of the cycle
    # advance fast pointer by that length
    # advance fast and slow pointers by 1 til they meet
    # where they meet is the start of the cycle 


findCycleStart()