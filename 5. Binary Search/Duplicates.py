
# You are given a sorted array A and a target T. Return the index where T would be placed if inserted in order.  if all elements are smaller than T, return A.length because that is where T should go


def findInsertionIndex(arr, target):
    pass

print(findInsertionIndex([1,2,3,3,3,5,6,8], 3)) # should return 5
print(findInsertionIndex([1,2,4,5,6,8], 3)) # should return 2
print(findInsertionIndex([1,2,4,5,6,8], 0)) # should return 0
print(findInsertionIndex([1,2,4,5,6,8], 4)) # should return 3

    
    # if not arr:
    #     return 0
    # if arr == None:
    #     return -1

    # start = 0
    # end = len(arr) - 1

    # while start <= end :
    #     mid = start + ((end - start) >> 1)
    #     if arr[mid] > target:
    #         if arr[mid-1] <= target:
    #             return mid
    #         end = mid - 1
    #     elif arr[mid] < target:
    #         if arr[mid+1] >= target:
    #             return mid
    #         start = mid + 1
    #     elif arr[mid] == target and arr[mid+1] != target:
    #         return mid + 1
    #     else:
    #         return len(arr)
    