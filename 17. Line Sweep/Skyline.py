# LC 218

# 1. (Level: Hard) Drawing the Skyline: You are given a list of buildings that are part of a skyline. For each building, you are given the height, start and end points. So if a building has [height=5, start=1, end=4], it represents a building of height 5 from point 1 on a number line to point 4.

# Given a list of such buildings that may overlap, you want to draw the skyline.

from typing import List 
import heapq
import collections

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ADD_BUILDING = 0
        REMOVE_BUILDING = 1

        unique_events = set()
        events = collections.defaultdict(list)

        for left, right, height in buildings:
            unique_events.add(left)
            unique_events.add(right)

            events[left].append((ADD_BUILDING, height))
            events[right].append((REMOVE_BUILDING, height))




# TEST CASE 

sol = Solution()
# output should be [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])) 

# output should be  [[0,3],[5,0]]
print(sol.getSkyline( [[0,2,3],[2,5,3]])) 