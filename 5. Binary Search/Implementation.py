#  Given a sorted array, search for a target item

def binary(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        # difference in middle from start or end
        mid = start + ((end - start) >> 1)
        # print(mid) #2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return -1
    

print(binary([1,2,4,8,9,10],4)) #should output #2
print(binary([1,2,4,8,9,10],3)) #should output -1