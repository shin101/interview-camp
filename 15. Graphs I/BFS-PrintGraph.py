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

# def level_order_traversal(tree):
#     if not tree: return
#     queue = collections.deque([tree])
#     currCount = 1
#     childrenCount = 0
#     while len(queue)!=0: 
#         curr = queue.popleft()
#         currCount-=1
#         print(curr.val, end=" ")
#         if curr.left:
#             queue.append(curr.left)
#             childrenCount+=1
#         if curr.right:
#             queue.append(curr.right)
#             childrenCount+=1
#         if currCount == 0:
#             print()
#             currCount, childrenCount = childrenCount, currCount

def levelOrder(root) -> List[List[int]]:
    list1=[]
    q=deque([root])

    while q:
        level=[]
        for i in range(len(q)):
            poping=q.popleft()
            if poping:
                level.append(poping.val)
                q.append(poping.left)
                q.append(poping.right)
        if level:
            list1.append(level)
    return list1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(level_order_traversal(root))


# --------- working solution -------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         queue = collections.deque([root]) # 
#         output = []

#         while queue:
#             level = [] 

#             for i in range(len(queue)):
#                 curr = queue.popleft()
#                 if curr:
#                     level.append(curr.val)
#                     queue.append(curr.left)
#                     queue.append(curr.right)
#             if level:
#                 output.append(level)
#         return output 

