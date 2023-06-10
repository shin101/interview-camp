# Given an array of positive and negative integers, find a subarray whose sum equals X.

# For example: Input = [2,4,-2,1,-3,5,-3], X = 5 --> Result = [2,4,-2,1].  Return the starting and ending indices of the subarray. Return null if array empty


# pseudo code : 
# initialize sum = 0 , map stores sum, index
# loop through, update sum, if sum == 0 then return 0,i
# if map contains sum then return map.get(sum)+1, i
# map.add(sum, i) if none of the if conditions are true


# def prefix_sum(input, target):
#     curr_sum = 0
#     cumulative_sum = {}

#     for idx,num in enumerate(input):
#         curr_sum += num
        
#         if num == target:
#             return [idx]
#         if curr_sum == target:
#             return [0,idx]

#         if num in cumulative_sum:
#             # print(cumulative_sum)
#             return [cumulative_sum[num]+1, idx]
        

#         cumulative_sum[num] = idx

#     return None


# print(prefix_sum([2,4,-2,1,-3,5,-3], 5)) # should return [0,3]
# # cumulative sum {2:0, 6:1, 4:2, 5:3, 2:4, 7:5, 4:6}
# print(prefix_sum([-1,2,2,-4,2,-1,4], 0)) # should return [1,3]
# print(prefix_sum([2, 1, 3, -1, -3, 7, -3], 1)) # should return None


# ------------------------------------------------------------

# my solution

def prefix_sum(input, target):
    dic = {} # same as cumulative sum
    # dic = {2:0, 6:1, 4:2, 5:3, ...} sum, idx
    sum = 0

    for idx, num in enumerate(input):
        sum += num
        if sum == target:
            return [0,idx]
        if sum in dic:
            return [dic[sum]+1, idx]
        dic[sum] = idx 
    return None

print(prefix_sum([2,4,-2,1,-3,5,-3], 5)) # should return [0,3]
# cumulative sum {2:0, 6:1, 4:2, 5:3, 2:4, 7:5, 4:6}
print(prefix_sum([-1,2,2,-4,2,-1,4], 0)) # should return [1,3]
print(prefix_sum([2, 1, 3, -1, -3, 7, -3], 1)) # should return [1]
# cumulative sum {2:0, 3:1, 6:2, 5:3, 2:4, 9:5, 6:6}