# Homework Problem 2 (Level: Medium)
# Print elements of a matrix in spiral order.

def spiralOrder(matrix):
    res = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    
    while len(res) != len(matrix) * len(matrix[0]) :
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not top < bottom or not left < right:
            break

        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -=1 

        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res



# test case

# [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# output should be [1,2,3,6,9,8,7,4,5]
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# [
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]
# ]
# output should be  [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# solution


# def spiralOrder(matrix):
#     res = []
#     left, right = 0, len(matrix[0])
#     top, bottom = 0, len(matrix)

#     while left < right and top < bottom: 
#         # get every i in the top row
#         for i in range(left, right):
#             res.append(matrix[top][i])
#         top += 1
        
#         # get every i in the right col
#         for i in range(top, bottom):
#             res.append(matrix[i][right - 1])
#         right -= 1

#         # need this condition for cases like [ 1, 2, 3]
#         if not (left < right and top < bottom):
#             break

#         for i in range(right - 1, left - 1, -1):
#             res.append(matrix[bottom - 1][i])
#         bottom -= 1

#         for i in range(bottom-1, top-1, -1):
#             res.append(matrix[i][left])
#         left += 1
#     return res



