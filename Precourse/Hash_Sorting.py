# Given an array of integers, find a pair of integers that sums to a number X. Use hash table.
# For e.g, if A = [6,3,5,2,1,7]. X = 4, Result= [3,1]

def find_pairs(lst, target):
    pass

print(find_pairs([6,3,5,2,1,7],4)) # should output [3,1]








# def find_pairs(lst, target):
#     dict = {}
#     # for num in lst, add to dict.
#     for num in lst:
#         dict[num] = target - num
    
#     for num in lst:
#         if target - num in dict:
#             return []


#     # if target - num in dict, return [target-num,num]


# print(find_pairs([6,3,5,2,1,7],4)) # should output [3,1]








# def find_pairs(lst,target):
#     obj = {}
#     for num in lst:
#         obj[num] = target - num

#     for num in lst:
#         if target - num in obj:
#             return [num, target - num]

#     return None

# # find_pairs([6,3,5,2,1,7],4)
# print(find_pairs([6,3,5,2,1,7],4)) # should output [3,1]




# O(N) time complexity. Trade off is hash maps take more space so for mobile for instance you might be better off using sort
