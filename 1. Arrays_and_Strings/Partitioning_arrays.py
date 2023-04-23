# Homework Problem (Level: Medium)
# Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are adjacent, with the colors in the order Red, White and Blue.
# Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).


# def sort_marbles(marbles):
#     pivot = 1
#     low_boundary = 0
#     high_boundary = len(marbles)-1
#     i =0

#     while i <= high_boundary:
#         if marbles[i] == pivot:
#             i+=1
#         elif marbles[i] > pivot:
#             marbles[i],marbles[high_boundary] = marbles[high_boundary],marbles[i]
#             high_boundary-=1
#         else:
#             marbles[i],marbles[low_boundary] = marbles[low_boundary],marbles[i]
#             low_boundary+=1
#             i+=1

#     return marbles


# print(sort_marbles([0,1,1,2,1,0,1,2])) # should return [0,0,1,1,1,1,2,2].

