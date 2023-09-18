# Homework Problem 1 (Level: Easy)

# Given a Binary Tree, print all paths from root to leaf.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        if not root:
            return 

        def recurse(node, res):
            res+=str(node.val)

            if not node.right and not node.left:
                output.append(res)
            if node.right:
                recurse(node.right, res+"->")
            if node.left:
                recurse(node.left, res+"->")


        recurse(root, "")
        return output

    