
# -------------Linked HashTable Notes-------------
# LL has O(n) lookup time
# Hashtable has no order. []
# To store LL in a hashtable, key=value of LL, value is pointer to the LL node
# This makes lookup O(1) and gives order to the hashtable

# >>> Least Recently Used (LRU) cache

# --------------------------------------------------

#              PROBLEM             : 
# Smallest Subarray Covering All Values: Let's say you are given a large text document Doc. You are also given a set S of words. You want to find the smallest substring of Doc that contains all the words in S. For example:

# Input : s = "ADOBECODEBANC", t = "ABC"
# Output : "BANC"

# hard

def minimum_window_substring(s, t):
    window, countT = {}, {}
    have, need = 0, len(t)
    length = float("inf")
    res = [0,0]
    left_pointer = 0

    for letter in t:
        countT[letter] = countT.get(letter, 0) + 1 # countT = {'A':1, 'B':1, 'C':1}
    
    for right_pointer in range(len(s)):
        char = s[right_pointer]
        window[char] = window.get(char, 0) + 1 # window = {'A':1, 'D':1, 'O':1, ...}
        if char in countT and window[char] == countT[char]:
            have += 1

        while have == need:
            if len(s[left_pointer:right_pointer]) < length:
                res = [left_pointer, right_pointer]
                length = len(s[left_pointer:right_pointer])
            window[s[left_pointer]] -= 1
            if s[left_pointer] in countT and window[ s[left_pointer]] < countT[ s[left_pointer]]:
                have -=1 
            left_pointer += 1
    left_pointer, right_pointer = res
    # print(s[left_pointer:right_pointer+1])
    return s[left_pointer:right_pointer+1] if length!=float("inf") else ""





# =============== WORKING SOLUTION ===============

# def minimum_window_substring(s, t):
#     if t == "": return ""
#     countT, window = {}, {}

#     for char in t:
#         countT[char] = 1 + countT.get(char, 0)

#     have, need = 0, len(countT)
#     res, resLen = [-1, -1], float("infinity")
#     left_pointer = 0

#     for right_pointer in range(len(s)):
#         char = s[right_pointer]
#         window[char] = 1 + window.get(char,0)

#         if char in countT and window[char] == countT[char]:
#             have += 1
        
#         while have == need:
#             # udpate result
#             if(right_pointer - left_pointer + 1) < resLen:
#                 res = [left_pointer, right_pointer]
#                 resLen = (right_pointer - left_pointer + 1)
#             # pop from the left of the window
#             window[s[left_pointer]] -= 1
#             if s[left_pointer] in countT and window[s[left_pointer]] < countT[s[left_pointer]]:
#                 have -= 1
#             left_pointer += 1
#     left_pointer, right_pointer = res
#     return s[left_pointer:right_pointer+1] if resLen != float("infinity") else ""


# ----------TEST CASE----------
def test_minimum_window_substring():
    # Test case 1: Unique minimum window substring
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    assert minimum_window_substring(s1, t1) == "BANC"

    # Test case 3: No valid window
    s3 = "xyz"
    t3 = "abc"
    assert minimum_window_substring(s3, t3) == ""

    # Test case 4: Unique minimum window substring with duplicates
    s4 = "ADOBECODEBANCAAAAA"
    t4 = "ABC"
    assert minimum_window_substring(s4, t4) == "BANC"

    # Test case 5: Unique minimum window substring with duplicates
    s5 = "aaabbbccc"
    t5 = "abc"
    assert minimum_window_substring(s5, t5) == "abbbc"

    # Test case 7: Empty string
    s7 = ""
    t7 = "abc"
    assert minimum_window_substring(s7, t7) == ""

    # Test case 10: Minimum window at the end of s
    s10 = "xyzjklmab"
    t10 = "ab"
    assert minimum_window_substring(s10, t10) == "ab"

    print("All test cases passed!")

test_minimum_window_substring()
