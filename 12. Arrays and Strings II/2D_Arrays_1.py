# Homework Problem 1 (Level: Medium)
# Print a 2D array in Diagonal ZigZag order.
# For example,Input:1 2 3 45 6 7 89 0 1 2
# Output:1 2 5 9 6 3 4 7 0 1 8 2


# def diagonal_zigzag_print(matrix):
#     pass





# -------- TEST CASE --------
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# output should be [1, 2, 5, 9, 6, 3, 4, 7, 0, 1, 8, 2]
print(diagonal_zigzag_print(matrix))
# output should be  [1,2,4,7,5,3,6,8,9]
print(diagonal_zigzag_print([[1,2,3],[4,5,6],[7,8,9]]) )
# output should be [1,2,3,4]
print(diagonal_zigzag_print([[1,2],[3,4]]) )

# -------- WORKING SOLUTION --------

# def diagonal_zigzag_print(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     res = []
#     # starting position at 0,0
#     curr_row = curr_col = 0
#     going_up = True

#     while len(res) != rows * cols :
#         if going_up:
#             while curr_row >= 0 and curr_col < cols:
#                 res.append(matrix[curr_row][curr_col])

#                 curr_row -= 1
#                 curr_col += 1
            
#             if curr_col == cols:
#                 curr_col -=1
#                 curr_row += 2
#             else:
#                 curr_row += 1
#             going_up = False
#         else:
#             while curr_row < rows and curr_col >= 0 :
#                 res.append(matrix[curr_row][curr_col])

#                 curr_col -= 1
#                 curr_row += 1

#             if curr_row == rows:
#                 curr_col += 2
#                 curr_row -=1 
#             else:
#                 curr_col += 1
#             going_up = True
        
#     return res
