# Homework Problem 1 (Level: Hard)
# Online Median: Given a stream of integers, find their median. If any integer is added to the stream, you should be able to update the median quickly.


# two heaps - large with minheap, small with maxheap
# heaps should be roughly same size


# test case

# solution 1 

# import heapq
# class MedianFinder: 
#     def __init__(self):
#         self.small, self.large = [], []

#     def addNum(self, num):
#         # push num to small heap first 
#         # python only implements minheap but small is maxheap
#         # multiply num by -1 to get around that and implement maxheap
#         heapq.heappush(self.small, -1 * num)

#         # make sure every num small is <= every num in large heap
#         if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)
        
#         # what if size is uneven - if difference is 2 or greater 
#         if len(self.small) > len(self.large) + 1:
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)
#         if len(self.large) > len(self.small) + 1:
#             val = heapq.heappop(self.large)
#             heapq.heappush(self.small, -1 * val)

#     def findMedian(self):
#         # if we have odd number of elements
#         if len(self.small) > len(self.large):
#             return -1 * self.small[0]
#         if len(self.large) > len(self.small):
#             return self.large[0]
#         return ((-1 * self.small[0] + self.large[0]) / 2)

