# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# HINT 
# first value of preorder is guaranteed to be a root because thats how it works 
# everything to the left of root in inorder is on left subtree, everything on the right is on right subtree 
# get the length of left and right subtree from inorder list and partition preorder list 
# recursively create left and right subtrees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def buildTree(preorder, inorder) :
#     pass


# SOLUTION
def buildTree(preorder, inorder) :
    # basecase
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid]) 
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root 

