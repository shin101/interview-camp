# (Level: Medium) Given a String, find the longest substring with unique characters.

# For example: "whatwhywhere" --> "atwhy"


# Return the start and end indexes of the substring.
# if the array is empty or null return null.
# shortest possible substring is just one character
# What to do if there are multiple longest substrings?
# Return any one of them.
# Do we have only alphabets? No, there can be any character




def longestStr(str) :
    if len(str)==0 or not str:
        return None
    result = [0,0]
    longest = 0 
    seen = set()
    start = 0
    end = 0
    idx = 0

    while start <= len(str):
        if end >= len(str):
            break
        if str[idx] not in seen:
            seen.add(str[idx])
            end += 1
            idx += 1
        elif str[idx] in seen:
            start += 1
        

    return result, longest


#     for idx in range(len(str)):
#         while str[idx] in str_set:
#             str_set.remove(str[start])
#             start += 1
#         str_set.add(str[idx])
#         result = max(result, idx-start+1)

    


print(longestStr("whatwhywhere")) # should return [2, 6]



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


