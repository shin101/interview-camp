# Homework Problem 1 (Level: Easy)

# Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order in O(n) time. For example:

# [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]

def traverse1(arr):
    output = []
    left = 0
    right = len(arr)-1

    while left <= right:
        if (abs(arr[left]) > abs(arr[right])):
            output.insert(0,arr[left]**2)
            left += 1
        elif(abs(arr[right]) > abs(arr[left])):
            output.insert(0, arr[right]**2)
            right -= 1
        else:
            output.insert(0,arr[left]**2)
            left+=1
    return(output)


print(traverse1([-4,-2,-1,0,3,5])) # should return [0,1,4,9,16,25]


# def traverse1(arr):
#     output = []
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         if abs(arr[left]) > abs(arr[right]):
#             output.insert(0,(arr[left])**2)
#             left +=1 
#         else:
#             output.insert(0,(arr[right])**2)
#             right -=1
#     return(output)


# print(traverse1([-4,-2,-1,0,3,5])) # should return [0,1,4,9,16,25]