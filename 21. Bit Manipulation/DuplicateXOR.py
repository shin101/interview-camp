# Given an array of integers where each element appears twice except one, find the element which appears once.
# For example: A = [3,7,3,5,5], Result = 7

def find_unique(arr):
    res = 0
    for idx in range(0,len(arr)):
        res^=arr[idx]
    return res


assert find_unique([3, 7, 3, 5, 5]) == 7
assert find_unique([1, 1, 2, 2, 3]) == 3
assert find_unique([4, 3, 2, 1, 2, 3, 1]) == 4
assert find_unique([0]) == 0
