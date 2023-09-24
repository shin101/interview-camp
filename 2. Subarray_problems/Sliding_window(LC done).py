# (Level: Medium) Given a String, find the longest substring with unique characters.

# For example: "whatwhywhere" --> "atwhy"


# Return the start and end indexes of the substring.
# if the array is empty or null return null.
# shortest possible substring is just one character
# What to do if there are multiple longest substrings?
# Return any one of them.
# Do we have only alphabets? No, there can be any character

def longestStr(string):
    seen = set()
    start = 0
    curr_len = 0
    max_len = 0
    output = [0,0]

    if not string:
        return None
    
    for idx in range(len(string)):
        if string[idx] not in seen:
            seen.add(string[idx])
            curr_len = idx - start + 1
            if curr_len > max_len:
                max_len = curr_len
                output = [start, idx]
        else:
            while string[idx] in seen:
                seen.remove(string[start])
                start += 1
            seen.add(string[idx])
    return output


print(longestStr("whatwhywhere")) # should return [2, 6]
print(longestStr("whayhkjfd")) # should return [2, 8]

# idx = 4
# seen = what
# seen = h
# start = 1
# output = [1,4]
# seen = hatw
















# def longestStr(string):
#     start = 0
#     curr_len = 0
#     max_len = 0
#     seen = set()
#     output = [0, 0]

#     if not string:
#         return None
    
#     for idx in range(len(string)):
#         # Growing window
#         if string[idx] not in seen:
#             seen.add(string[idx])
#             curr_len = idx - start + 1

#             if curr_len > max_len:
#                 output = [start, idx]
#                 max_len = curr_len

#         # Shrinking window
#         else:
#             curr_char = string[idx]
#             while curr_char in seen:
#                 seen.remove(string[start])
#                 start += 1
#             seen.add(curr_char)

# # whayhkjfd
#     return output




# HINT : 
    # declare result = [0,0] and longest 
    # iterate thru every letter , while char in the set, remove that char and increment start idx
    # otherwise, add to set. if current string length is bigger than longest variable, then
    # update longest and also result 





# ------------------------------------------------
# ANSWER BELOW 
# ------------------------------------------------




# THIS WILL RETURN START & END INDICES OF SUBSTRING, WHICH IS WHAT WE WANT 
# def longestStr(str) :
#     if not str:
#         return None
    
#     start = 0
#     str_set = set()
#     result = [0, 0] # initialize result as a list with start and end indexes
#     longest = 0

#     for idx in range(len(str)):
#         while str[idx] in str_set:
#             str_set.remove(str[start])
#             start += 1
#         str_set.add(str[idx])
#         if idx - start + 1 > longest:
#             longest = idx - start + 1
#             result = [start, idx]

#     return result


# print(longestStr("whatwhywhere")) # should return [2, 6]


# THIS WILL RETURN LENGTH OF UNIQUE STR
# def longestStr(str) :
#     if not str:
#         return None
    
#     start = 0
#     str_set = set()
#     result = 0

#     for idx in range(len(str)):
#         while str[idx] in str_set:
#             str_set.remove(str[start])
#             start += 1
#         str_set.add(str[idx])
#         result = max(result, idx-start+1)


#     return result # this will return number of string




# print(longestStr("whatwhywhere")) 


