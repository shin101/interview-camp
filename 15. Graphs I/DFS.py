# Homework Problem 1 (Level: Hard)

# Clone a Graph: Given an directed graph, make a copy.

# Hint: The trick here is to maintain a map of old nodes to their corresponding new nodes. This will ensure that any cycles are handled.

# Note: This can be solved with either DFS or BFS.

# step 1 clone
# step 2 map old node to the new node in hash map. DFS uses recursion

class Node:
  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #  hash map or list, for storing output
        # DFS - recursion

        newToOld = { } 

        def dfs(node):
            if node in newToOld:
                return newToOld[node]
        
            copy = Node(node.val)
            newToOld[node] = copy

            # neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None

  
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         oldToNew = {}

#         def dfs(node):
#             if node in oldToNew: 
#                 return oldToNew[node]
#             copy = Node(node.val)
#             oldToNew[node] = copy
#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei)) 
#             return copy
        
#         return dfs(node) if node else None




# Test Case
# TEST ON LEETCODE








# DFS Solution

# class Node:
#   def __init__(self, val=0, neighbors=None):
#     self.val = val
#     self.neighbors = neighbors if neighbors is not None else []

# def cloneGraph(node):
#   oldToNew = {}

#   def dfs(node):
#     if node in oldToNew: # if we already made a clone of it
#       return oldToNew[node]
#     # clone 
#     copy = Node(node.val)
#     oldToNew[node] = copy
#     for nei in node.neighbors:
#       # clone neighbors recursively 
#       # dfs(nei) returns copy it created and now append to list of neighbors 
#       copy.neighbors.append(dfs(nei)) 
#     return copy
  
#   return dfs(node) if node else None



# Solution that passes on Leetcode
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         oldToNew = {}

#         def dfs(node):
#             if node in oldToNew: 
#                 return oldToNew[node]
#             copy = Node(node.val)
#             oldToNew[node] = copy
#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei)) 
#             return copy
        
#         return dfs(node) if node else None