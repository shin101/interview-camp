# Coin Change Problem: Given a set of coin denominations, print out the different ways you can make a target amount. You can use as many coins of each denomination as you like.

# Variant of this problem: If you had to print just the count (instead of the actual combinations), there is a more efficient solution in the Dynamic Programming Section. This solution is also acceptable though.

def print_coins():
    pass


print(print_coins([1,2,5],5)) 
# output will be [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]






# def print_coins(arr, target):
#     if len(arr)==0:
#         return None
#     print_coins_helper(arr, target, 0, [], 0)


# def print_coins_helper(arr, target, start_index, buffer, sum):
#     if sum > target:
#         return 
#     if sum == target:
#         print(buffer)
#         return
    
#     for idx in range(start_index, len(arr)):
#         buffer.append(arr[idx])
#         print_coins_helper(arr, target, idx, buffer, sum+arr[idx])
#         buffer.pop()


print(print_coins([1,2,5],5)) 
# output will be [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]



# ------------------------------------------------------------------------------
# Working solution


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
# output will be [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]