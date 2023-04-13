# Given an array of integers that can be both +ve and -ve, find the contiguous subarraywith the largest sum.
# For example:  [1,2,-1,2,-3,2,-5]  -> first 4 elements have the largest sum. Return (0,3)


def maximumSumSubarray(lst):
    curr = lst[0]
    max_sum = lst[0]

    for num in lst[1:]: 
        curr = max(num, curr+num)
        max_sum =  max(max_sum, curr)
    return max_sum
    
# curr = max(2, -1) now curr is 2
# max_sum = max(3) # now max_sum is 3

print(maximumSumSubarray([1,2,-1,3,4,10,10,-10,-1])) # should return 29
print(maximumSumSubarray([1,2,-1,3,4,-1])) # should return 9
print(maximumSumSubarray([-1,1])) # should return 1

























#  for (int i = 1; i < a.length; i++) {        
# maxEndingHere = Math.max(maxEndingHere + a[i], a[i]);        
# maxSum = Math.max(maxSum, maxEndingHere);    }