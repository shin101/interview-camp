# Homework Problem 1 (Level: Easy)

# Print Graph in Level Order: Given a graph and a node N, print the Graph in order of distance from N. All nodes of distance 1 from N, followed by nodes of distance 2 from N, etc.

# BFS uses queue

# Similar Problem: Print a tree in level order.

import collections

class Node:
    def __init__(self, val, right=0, left=0):
        self.val = val
        self.right = right
        self.left = left

def level_order_traversal(tree):
    if not tree: return
    queue = collections.deque([tree])
    currCount = 1
    childrenCount = 0
    while len(queue)!=0: 
        curr = queue.popleft()
        currCount-=1
        print(curr.val, end=" ")
        if curr.left:
            queue.append(curr.left)
            childrenCount+=1
        if curr.right:
            queue.append(curr.right)
            childrenCount+=1
        if currCount == 0:
            print()
            currCount, childrenCount = childrenCount, currCount


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(level_order_traversal(root))

