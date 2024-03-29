# 215. Kth Largest Element in an Array
# Medium


# Use quick select algorithm, which is like quicksort but uses divide-and-conquer

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# step 1 - find pivot (random num)
# step 2 - partition around the pivot
# step 3 - if we found target index return otherwise recurse


def findKthLargest(nums, k):
    pass
# USE HEAPS  not select algorithm 

# test case

print(findKthLargest([3,2,1,5,6,4], 2)) # 5

# pivot = 4
# if 3 <= 4 : [4, 2, 1, 5, 6, 3]. pointer = 1
# [4, 3, 1, 5, 6, 2]
# 

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4

# solution
# USE HEAPS TO PASS LC TEST CASE



# SELECT ALGO, BELOW CODE WONT PASS TEST CASES ON LC
# def findKthLargest(nums, k ):
#     k = len(nums) - k # index if array was sorted

#     def quickSelect(l,r):
#         pivot, p = nums[r], l # p for pointer
#         for i in range(l,r):
#             if nums[i] <= pivot:
#                 nums[p], nums[i] = nums[i], nums[p]
#                 p += 1
#         nums[p], nums[r] = nums[r], nums[p]

#         if p > k:
#             return quickSelect(l, p - 1)
#         elif p < k :
#             return quickSelect(p + 1, r)
#         else:
#             return nums[p]
#     return quickSelect(0, len(nums) - 1)