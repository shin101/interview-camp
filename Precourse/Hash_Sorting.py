


# Given an array of integers, find a pair of integers that sums to a number X. Use hash table.
# For e.g, if A = [6,3,5,2,1,7]. Target = 4, Result= [3,1]
# part 1 - use hash set

# def find_pairs(arr, target):
#     seen = set() #-2,1, -1, 2, 
#     for num in arr:
#         if num not in seen : 
#             seen.add(target-num)
#         else : 
#             return [num, target-num]
#     return None

# print(find_pairs([6,3,5,2,1,7],4))


# part 2 - return index pos of pairs 
# For e.g, if A = [6,3,5,2,1,7]. Target = 4, Result= [1,4]

def find_pairs(arr, target):
    dict = {} # key = num-target ; value = position
    # {-2:0, 1:1, -1:2, 2:3, ...}
    idx = 0
    for num in arr:
        if num in dict:
            return [dict[num] , idx]
        else:
            dict[target-num] = idx
        idx += 1 


print(find_pairs([6,3,5,2,1,7], 4))








# {-2: 0, 1: -2, 1: 2}

# Return index pos of pairs
# def find_pairs(lst, target):
#     d = {}
#     for i, num in enumerate(lst):
#         if num in d:
#             return [d[num], i]
        
#         d[target - num] = i


    # return value of pairs
    # s = set()

    # for num in lst:
    #     if num in s:
    #         return [target - num, num]
        
    #     s.add(target - num)

    # return None



# print(find_pairs([6,5,3,2,1,7], 4)) # should output [1, 4]








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
