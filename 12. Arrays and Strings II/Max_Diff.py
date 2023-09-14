# Level: Hard
# Leetcode 123. Best Time to Buy and Sell Stock III

# Given a list of stock prices for a company, find the maximum amount of money you can make with two trades. A trade is a buy and sell.The two trades cannot overlap.


# def maxProfit(prices):
#     pass

# # test case
# print(maxProfit([3,3,5,0,0,3,1,4])) # should be 6
# print(maxProfit([1,2,3,4,5])) # should be 4
# print(maxProfit( [7,6,4,3,1])) # should be 0


# solution 

# def maxProfit(prices) -> int:
#     if not prices:
#         return 0
    
#     A = -prices[0] # when you buy you are losing money hence the - sign 
#     B = float('-inf') # you are waiting to buy the stock
#     C = float('-inf')
#     D = float('-inf')

#     for price in prices:
#         A = max(A, -price) # either stay in A position or you can buy (-price)
#         B = max(B, A + price) # sell
#         C = max(C, B - price) # buy
#         D = max(D, C + price) # sell
#         print('A is', A)
#         print('B is',B)
#         print('C is',C)
#         print('D is',D)
#     return D 

                     
# print(maxProfit([3,3,5,0,0,3,1,4])) # should be 6
# print(maxProfit([1,2,3,4,5])) # should be 4
# print(maxProfit( [7,6,4,3,1])) # should be 0