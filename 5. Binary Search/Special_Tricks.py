# Homework Problem 1 (Level: Easy)

# Find the square root of an integer X. For example, squareRoot(4) = 2. It is ok to find the integer floor of the square root. So squareRoot(5) or squareRoot(8) can also return 2. squareRoot(9) will return 3.

# Using Binary Search, you can search for square roots over the integer space. This is pretty fast because it takes O(log(n)) time. Assume that x*x is less than the integer limit.

# def square_root(x):
#     low = 0
#     high = x-1
#     arr = list(range(x)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     # print (arr)

#     while low <= high:
#         mid = low + ((high-low) >> 1)
#         if arr[mid] ** 2 == x:
#             return mid
#         if arr[mid] ** 2 > x:
#             high = mid - 1 
#         if arr[mid] ** 2 < x:
#             if arr[mid+1] **2 > x:
#                 return mid
#             low = mid + 1
#     return -1


# def test_square_root():
#     # Test cases where the square root is an integer
#     assert square_root(4) == 2
#     assert square_root(9) == 3
#     assert square_root(16) == 4
#     assert square_root(25) == 5

#     # Test cases where the square root is not an integer (return floor value)
#     assert square_root(5) == 2
#     assert square_root(8) == 2
#     assert square_root(15) == 3
#     assert square_root(26) == 5

#     # Test case with a large number
#     assert square_root(1000000) == 1000

#     # Test case with a negative number 
#     assert square_root(-3) == -1


#     print("All test cases passed!")


# test_square_root()


# Homework Problem 2 (Level: Medium)

# Search for a Peak: A peak element in array A is an A[i] where its adjacent elements are less than A[i]. So, A[i - 1] < A[i] and A[i + 1] < A[i].

# Assume there are no duplicates. Also, assume that A[-1] and A[length] are negative infinity (-∞). So A[0] can be a peak if A[1] < A[0].

# A = [1,3,4,5,2] => Peak = 5
# A = [5,3,1] => Peak = 5
# A = [1,3,5] => Peak = 5