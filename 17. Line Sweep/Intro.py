# Homework Problem 1 (Level: Medium)
# 1. Merge Intervals - Given a list of intervals, merge all overlapping intervals. At the end of the merge, there should be no overlapping intervals.

# For example,
# Input = (1,3), (3,5), (6,8), (7,9)
# Output = (1,5), (6,9)


# step 1 : sort by start point
# step 2 : define last ending point
# step 3 : decide whether to merge or not 


def merge( intervals):
    
    intervals.sort(key=lambda x:x[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start,end])

    return output

# TEST CASE
print(merge([[1,3],[2,6],[8,10],[15,18]])) # output : [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]])) # output : [[1,5]]



# SOLUTION 

# def merge(intervals):
#     intervals.sort(key = lambda i : i[0])
#     output = [intervals[0]]
    
#     for start, end in intervals[1:]:
#         lastEnd = output[-1][1]

#         if start <= lastEnd:
#             # we do max in case your intervals look something like [1,5], [2,4]
#             output[-1][1]= max(lastEnd, end)
#         else:
#             output.append([start, end])
#     return output


# chatGPT alternative
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort(key=lambda x: x[0])

    #     output = []

    #     for start, end in intervals:
    #         if not output or start > output[-1][1]:
    #             output.append([start, end])
    #         else:
    #             output[-1][1] = max(output[-1][1], end)

    #     return output
