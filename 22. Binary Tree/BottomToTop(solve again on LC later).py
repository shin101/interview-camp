# Homework Problem 1 
# Leetcode 543 - Easy

# Find the Diameter of a Binary Tree. The Diameter is the longest path from any 2 nodes in the tree. 

# hint - recursion, height = 1 + max(left, right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def diameterOfBinaryTree(root) -> int:
        # height = 1 + max(left, right)
        # diameter = left + right + 2 
        res = [0]

        def dfs(root):
            if not root: 
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max ((2 + left + right), res[0])

            return 1 + max(left, right)
        dfs(root)
        return res[0]


sol = TreeNode()
# TESTCASE (test on LC)
print(sol.diameterOfBinaryTree([1,2,3,4,5])) # output should be 3
print(sol.diameterOfBinaryTree([1,2])) # output should be 1
# diameter = 0,
# height = 0,

