# Homework Problem 2 (Level: Medium) - Very Commonly Asked

# Word Ladder Problem: You are given 2 words A and B, both of the same length. Your task is to transform one word to another changing only one letter each time. Each intermediate word should be a valid word in the dictionary. Print out the length of the path. (Alternate version: print out the intermediate words)

# A = CAB, B = DOG
# Result: 4 (CAB -> COB -> COG -> DOG)

from collections import deque
#     # one char diff
#     # create queue 

def oneCharDiff(word1, word2):
    cnt = 0
    for letter1,letter2 in zip(word1,word2):
        if letter1!=letter2:
            cnt += 1
    return cnt == 1

def wordLadder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = set()

    while queue:
        word, depth = queue.popleft()
        if word == endWord:
            return depth
        
        visited.add(word)
        
        for next_word in wordList:
            if next_word not in visited and oneCharDiff(word, next_word):
                queue.append((next_word, depth+1))
    
    return 0

# TEST CASE

print(wordLadder("CAB", "DOG", ["CAB", "COB", "COG", "DOG"])) # should return 4
# should return 5
print(wordLadder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

# # Test case
# start_word = "hit"
# end_word = "cog"
# word_dictionary = set(["hot", "dot", "dog", "lot", "log", "cog"])
# print(wordLadder(start_word, end_word, word_dictionary))  # Output: 5



# SOLUTION 1
# from collections import deque
# Function to check if two words differ by only one character
# def is_one_letter_apart(word1, word2):
#     diff_count = 0
#     for c1, c2 in zip(word1, word2):
#         if c1 != c2:
#             diff_count += 1
#             if diff_count > 1:
#                 return False
#     return diff_count == 1

# Function to find the shortest transformation path length
# def word_ladder_length(start, end, word_list):
#     if end not in word_list:
#         return 0
    
#     queue = deque([(start, 1)])  # Queue of words and their corresponding depths
#     visited = set()

#     while queue:
#         word, depth = queue.popleft()

#         if word == end:
#             return depth
        
#         visited.add(word)
        
#         for next_word in word_list:
#             if next_word not in visited and is_one_letter_apart(word, next_word):
#                 queue.append((next_word, depth + 1))

#     return 0  # No transformation path found



# # SOLUTION  2
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
