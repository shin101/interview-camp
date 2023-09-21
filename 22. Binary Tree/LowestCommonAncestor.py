# 236. Lowest Common Ancestor of a Binary Tree
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Use DFS - recursion, basecase, 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None

        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node ==p or node ==q 
            if (left and right) or (cur and right) or (cur and left):
                self.answer = node
                return
            return left or right or cur
        dfs(root)
        return self.answer
            
# Test Case

# just test on LC 


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()
p = root.left
q = root.right
print(sol.lowestCommonAncestor(root, p, q).val) # output = 3

p = root.left
q = root.left.right.right
print(sol.lowestCommonAncestor(root, p, q).val)  # Output: 5





# SOLUTION 

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         self.answer = None

#         def dfs(node):
#             if not node:
#                 return False
#             left = dfs(node.left)
#             right = dfs(node.right)
#             cur = node ==p or node ==q 
#             if (left and right) or (cur and right) or (cur and left):
#                 self.answer = node
#                 return
#             return left or right or cur
#         dfs(root)
#         return self.answer
            