# Leetcode 36 , Medium, Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# HINT : 
# Hash map where key is col # and value is set 

# def isValidSudoku(board) -> bool:
#     import collections
#     pass

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)] # idx : location, val: number
        cols = [set() for i in range(9)] 
        squares = [set() for i in range(9)] 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3 * 3 + c//3]:
                    return False
        
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3 * 3 + c//3].add(board[r][c])
        return True
                

# Test case - test on leetcode 
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# true
print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# false 


# Solution 

# List Solution

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [set() for i in range(9)]
#         cols = [set() for i in range(9)]
#         squares = [set() for i in range(9)]

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3 * 3 +  c//3] :
#                     return False
        
#                 rows[r].add(board[r][c])
#                 cols[c].add(board[r][c])
#                 squares[r//3 * 3 +  c//3].add(board[r][c])
                
#         return True
                


# Dict Solution

# def isValidSudoku(board) -> bool:
#     import collections
#     # using hashmap where key is col # and value is set 
#     cols = collections.defaultdict(set) # creates a dictionary where all keys default to empty sets
#     rows = collections.defaultdict(set)
#     squares = collections.defaultdict(set) # key = (r/3, c/3)

#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == ".":
#                 continue
#             if (board[row][col] in rows[row] or 
#                 board[row][col] in cols[col] or 
#                 board[row][col] in squares[(row//3, col//3)]
#                 ):
#                 return False
            
#             cols[col].add(board[row][col])
#             rows[row].add(board[row][col])
#             squares[(row//3, col//3)].add(board[row][col])
    
#     return True