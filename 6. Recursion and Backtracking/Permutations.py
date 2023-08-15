# Coin Change Problem: Given a set of coin denominations, print out the different ways you can make a target amount. You can use as many coins of each denomination as you like. For example: If coins are [1,2,5] and the target is 5, output will be: [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]

# Variant of this problem: If you had to print just the count (instead of the actual combinations), there is a more efficient solution in the Dynamic Programming Section. This solution is also acceptable though.

# HINT : 
# 1. determine termination cases
# 2. find candidates
# 3. place them into buffer index
# 4. recurse to next index

def print_coins(coins, target):
    pass



print(print_coins([1,2,5],5)) 
# output will be [1,1,1,1,1], [1,1,1,2], [1,2,2], [5] for recursive, 1 for DP

# -----------------------------------------------------------------------------
# Working solution 1 - DP Solution

# def print_coins(target, coins, known_results):
#     min_coins = target

#     # base case
#     if target in coins:
#         known_results[target] = 1
#         return 1 
#     #return a known result if its greater than 1 
#     elif known_results[target] > 0 :
#         return known_results[target]
#     else:
#         # for every coin value that is <= target  
#         for val in [coin for coin in coins if coin<=target]:
#             num_coins = 1 + print_coins(target-val, coins, known_results)
#             if num_coins < min_coins :
#                 min_coins = num_coins
#                 known_results[target] = min_coins
#     return min_coins

# print_coins(74, [1,5,10,25], [0]*(target+1))
# should return 8

# -----------------------------------------------------------------------------
# Working solution 2 - from Interview Camp, Recursive Solution


# def printCoins(coins, target):
#     if coins is None or len(coins) == 0 or target <= 0:
#         return
#     printCoinsHelper(coins, target, 0, [], 0)

# def printCoinsHelper(coins, target, startIndex, buffer, sum):
#     # Termination cases
#     if sum > target:
#         return
#     if sum == target:
#         print(buffer)
#         return

#     # Find candidates that go into the buffer
#     for i in range(startIndex, len(coins)):
#         # Place candidate into the buffer and recurse
#         buffer.append(coins[i])
#         printCoinsHelper(coins, target, i, buffer, sum + coins[i])
#         buffer.pop()

# print(printCoins([1,2,5],5)) 
# output will be [1,1,1,1,1], [1,1,1,2], [1,2,2], [5] for recursive, 1 for DP
