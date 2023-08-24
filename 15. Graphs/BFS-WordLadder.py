# Homework Problem 2 (Level: Medium) - Very Commonly Asked

# Word Ladder Problem: You are given 2 words A and B, both of the same length. Your task is to transform one word to another changing only one letter each time. Each intermediate word should be a valid word in the dictionary. Print out the length of the path. (Alternate version: print out the intermediate words)

# A = CAB, B = DOG
# Result: 4 (CAB -> COB -> COG -> DOG)
from collections import collections, deque, defaultdict

# def wordLadder(beginWord, endWord, WordList):
#     # https://www.youtube.com/watch?v=EAcJgd4Xu5E
#     # write a function to check if one char is different
#     # create a graph using that function
#     # bfs queue
#     pass

def wordLadder(beginWord, endWord, WordList):
    def onechar(s,t):
        if s == t : 
            return False
        cnt = 0
        for i in range(len(s)):
            if s[i] != t[i]: cnt+=1
        return cnt == 1
    
    graph = defaultdict(set)
    for s in WordList+[beginWord]:
        for t in WordList+[beginWord]:
            if onechar(s,t):
                graph[s].add(t)

    q = deque([(beginWord, 0)])

# # Test case
# start_word = "hit"
# end_word = "cog"
# word_dictionary = set(["hot", "dot", "dog", "lot", "log", "cog"])
# print(wordLadder(start_word, end_word, word_dictionary))  # Output: 5


# SOLUTION 1 
# https://www.youtube.com/watch?v=EAcJgd4Xu5E





# # SOLUTION 2
# def wordLadder(beginWord, endWord, wordList):
#     if endWord not in wordList:
#         return 0
#     # its a dictionary where you insert a new value for the first time default value will be an empty list 
#     neighbors = collections.defaultdict(list)
#     wordList.append(beginWord)
#     for word in wordList:
#         for j in range(len(word)):
#             pattern = word[:j] + "*" + word[j+1:]
#             neighbors[pattern].append(word)

#     visit = set([beginWord])
#     q = deque([beginWord])
#     res = 1
#     while q:
#         for i in range(len(q)):
#             word = q.popleft()
#             if word == endWord:
#                 return res
#             for j in range(len(word)):
#                 pattern = word[:j] + "*" + word[j+1:]
#                 for neiWord in neighbors[pattern]:
#                     if neiWord not in visit:
#                         visit.add(neiWord)
#                         q.append(neiWord)
#         res +=1
#     return 0 
