# Homework Problem 1 (Level: Hard)
# 239. Sliding Window Maximum


# Maximum of Sliding Window: Given an array A and an integer K, find the maximum element in each sliding window of size K. For example:

# A = [4,6,5,2,4,7] and K = 3, windows are as follows:

# [4,6,5,2,4,7] : Max = 6
# [4,6,5,2,4,7] : Max = 6
# [4,6,5,2,4,7] : Max = 5
# [4,6,5,2,4,7] : Max = 7

# Output: 6,6,5,7

# Hint: You can do this in O(n) time, by using the Queue with Max we implemented above.

# sliding window so you need left and right pointers
# define output [] and deque (which stores indices
# process while right pointer has not reached len(nums)
# pop from queue if nums[q[-1]] < nums[r]
# append right value to q
# remove left val from window if left is bigger than q[0]

import collections

def maxSlidingWindow(nums, k):
    output = []
    l = r = 0
    q = collections.deque()

    while r < len(nums):
        while q and nums[r] > nums[q[-1]]:
            q.pop()
        q.append(r)

        if q[0] < l:
            q.popleft()

        if (r+1) >= k :
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output



# Test Case
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # should output [3,3,5,5,6,7]
print(maxSlidingWindow([1], 1)) # should output [1]




# Solution

# def maxSlidingWindow(nums, k):
#     output = [] 
#     q = collections.deque() # contains indices 
#     l = r = 0

#     while r < len(nums):
#         # pop smaller values from q 
#         while q and nums[q[-1]] < nums[r]: # store index, rather than value, in the deque
#             q.pop()
#         q.append(r)

#         # remove left val from window (we just shifted window)
#         if l > q[0]:
#             q.popleft()
        
#         if (r+1) >= k:
#             output.append(nums[q[0]])
#             l += 1
#         r += 1
#     return output 
