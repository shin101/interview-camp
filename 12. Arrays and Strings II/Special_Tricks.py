# Homework Problem 1 (Level: Easy)
# Rotate an array A by X items. For example,
# A = [1,2,3,4,5,6] and X = 2, Result = [5,6,1,2,3,4]

# Hint: Use same trick we used in "Reverse Words of a Sentence" above.
# reverse everything, then reverse each word 

def rotate(arr, k):
    k = k%len(arr)
    l, r = 0, len(arr)-1
    while l < r :
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

    l,r = 0, k-1
    while l < r :
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    
    l,r = k, len(arr)-1
    while l < r :
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

    return arr

# [7, 6, 5, 4, 3, 2, 1]

# test case
print(rotate([1,2,3,4,5,6,7],3)) # Output: [5,6,7,1,2,3,4]
print(rotate([-1,-100,3,99],2)) # Output: [3,99,-1,-100]