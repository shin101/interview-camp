from typing import Optional

# Leetcode 109
# same as LC 108 sorted array BST but this is LL
# turn it into array from LL 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        node = head

        while node:
            arr.append(node.val)
            node = node.next
        
        def make(l,r):
            if l<=r :
                mid = (l+r) // 2
                node = TreeNode(arr[mid])
                node.left = make(l, mid-1)
                node.right = make(mid+1, r)
                return node
        return make(0, len(arr)-1)
        


    # solution 1 
    # class Solution:
    # def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #     if not head: return None

    #     n = 0
    #     cur = head 
    #     while cur : 
    #         cur = cur.next 
    #         n += 1
        
    #     self.head = head

    #     def rec(st, end):
    #         if st>end : return None
    #         # left
    #         mid = (st+end)//2
    #         left = rec(st, mid-1)
    #         # root 
    #         root = TreeNode(self.head.val)
    #         self.head = self.head.next
    #         root.left = left

    #         # right
    #         root.right = rec(mid+1, end)
    #         return root
    
    #     return rec(0, n-1)