from typing import List
# 300. Longest Increasing Subsequence

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# This is a DP question


# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


# hint 
# iterate backwards, need condition for increasing order, cache repeated work 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) # cache

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        
        return max(LIS)
    
# test case
sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4 